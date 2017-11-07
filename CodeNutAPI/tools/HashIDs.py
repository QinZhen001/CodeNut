#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


class HashIDs:
    __alphabet = 'xcS4F6h89aUbideAI7tkynuopqrXCgTE5GBKHLMjfRsz'
    __primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    __minHashLength = 0

    def __init__(self, salt='the quick brown fox jumps over the lazy dog', min_hash_length=0, alphabet=None):
        if not isinstance(salt, str):
            raise ValueError('Salt should be a string')

        self.__salt = salt

        if min_hash_length is not None and isinstance(min_hash_length, int) and min_hash_length > 0:
            self.__minHashLength = min_hash_length

        if alphabet is not None and isinstance(alphabet, str) and len(alphabet) > 0:
            if len(alphabet) < 4:
                raise ValueError(
                    'The alphabet should contain at least 4 unique symbols')

            # Make sure the user created alphabet only contains unique values
            self.__alphabet = ''.join(set(alphabet))

        self.__guards = []
        self.__seps = []

        for prime in self.__primes:
            if prime - 1 > len(self.__alphabet):
                break

            character = self.__alphabet[prime - 1]
            self.__seps.append(character)
            self.__alphabet = self.__alphabet.replace(character, ' ')

        for index in [0, 4, 8, 12]:
            if index > len(self.__seps):
                break

            sep = self.__seps[index]
            self.__guards.append(sep)
            self.__seps.remove(sep)

        self.__alphabet = self.__alphabet.replace(' ', '')
        self.__alphabet = self.__shuffle(self.__alphabet, self.__salt)

    def encrypt(self, *values):
        ret = ''

        if len(values) == 0:
            return ret

        for number in values:
            if not isinstance(number, int) or number < 0:
                return ret

        return self.__encode(values, self.__alphabet, self.__salt, self.__minHashLength)

    def decrypt(self, hashed_id):
        if not hashed_id or not isinstance(hashed_id, str):
            raise ValueError('hashed_id should be a string')
        return self.__decode(hashed_id)

    def __encode(self, values, alphabet, salt, min_hash_length):
        ret = ''

        seps = list(self.__shuffle(self.__seps, values))

        for idx, val in enumerate(values):
            lotteryChar = ''
            if not idx:
                lotterySalt = '-'.join('%d' % value for value in values)
                for subNumber in values:
                    lotterySalt += '-' + str((subNumber + 1) * 2)

                lottery = self.__shuffle(alphabet, lotterySalt)
                lotteryChar = lottery[0]
                ret += lotteryChar

                alphabet = lotteryChar + alphabet.replace(lotteryChar, '')

            alphabet = self.__shuffle(alphabet, str(
                (ord(lotteryChar) & 12345)) + salt)
            ret += self.__hash(val, alphabet)

            if idx + 1 < len(values):
                sepsIndex = (val + idx) % len(seps)
                ret += seps[sepsIndex]

        if len(ret) < min_hash_length:
            firstIndex = 0
            for idx, val in enumerate(values):
                firstIndex += (idx + 1) * val

            guardIndex = firstIndex % len(self.__guards)
            guard = self.__guards[guardIndex]

            ret = guard + ret
            if len(ret) < min_hash_length:
                guardIndex = (guardIndex + len(ret)) % len(self.__guards)
                guard = self.__guards[guardIndex]

                ret += guard

        while len(ret) < min_hash_length:
            padList = [str(ord(alphabet[1])), str(ord(alphabet[0]))]

            padLeft = self.__encode(padList, alphabet, salt, min_hash_length)
            padRight = self.__encode(
                padList, alphabet, ''.join(padList), min_hash_length)

            ret = padLeft + ret + padRight
            excess = len(ret) - min_hash_length

            if excess > 0:
                trim = excess / 2
                ret = ret[trim:min_hash_length + trim]

            alphabet = self.__shuffle(alphabet, salt + ret)

        return ret

    def __decode(self, hashed_id):
        ret = []

        if len(hashed_id):
            originalHash = hashed_id

            hashed_id = re.sub('[%s]' % ''.join(self.__guards), '', hashed_id)
            hashExplode = hashed_id.split(' ')

            i = 0
            if len(hashExplode) == 3 or len(hashExplode) == 2:
                i = 1

            hashed_id = hashExplode[i]

            hashed_id = re.sub('[{}]'.format(
                ''.join(self.__seps)), ' ', hashed_id)
            hashArray = hashed_id.split(' ')

            alphabet = ''
            lotteryChar = ''

            for idx, subHash in enumerate(hashArray):
                if len(subHash):
                    if not idx:
                        lotteryChar = hashed_id[0]
                        subHash = subHash[1:]
                        alphabet = lotteryChar + \
                            self.__alphabet.replace(lotteryChar, '')

                    alphabet = self.__shuffle(alphabet, str(
                        ord(lotteryChar) & 12345) + self.__salt)
                    number = self.__dehash(subHash, alphabet)
                    ret.append(number)

            encryptResult = self.encrypt(*ret)
            if encryptResult != originalHash:
                ret = []
        return ret

    @staticmethod
    def __shuffle(alphabet, salt):
        if isinstance(alphabet, list):
            alphabet = ''.join(alphabet)

        if isinstance(salt, list):
            salt = ''.join(salt)

        if isinstance(salt, tuple):
            salt = ''.join('%d' % num for num in salt)

        if alphabet:
            alphabetList = list(alphabet)

            sortingList = [ord(character) for character in salt]

            for i in range(len(sortingList)):
                add = True
                for k in range(i, len(sortingList) + i - 1):
                    nextIndex = (k + 1) % len(sortingList)
                    if add:
                        sortingList[i] += sortingList[nextIndex] + (k * i)
                    else:
                        sortingList[i] -= sortingList[nextIndex]
                    add = not add
                sortingList[i] = abs(sortingList[i])

            i = 0
            ret = ''
            sortingArraySize = len(sortingList)
            while len(alphabetList) > 0:
                size = len(alphabetList)
                pos = sortingList[i]

                if pos >= size:
                    pos = pos % size

                ret += alphabetList.pop(pos)

                i = (i + 1) % sortingArraySize
            return ret
        return None

    @staticmethod
    def __hash(data, alphabet):
        hashed_id = ''
        alphabetLength = len(alphabet)

        while True:
            index = (data % alphabetLength)

            hashed_id = alphabet[index] + hashed_id
            data = int(data / alphabetLength)

            if not data:
                break
        return hashed_id

    @staticmethod
    def __dehash(data, alphabet):
        number = 0

        if len(data) and alphabet:
            alphabetLength = len(alphabet)
            inputChars = data[::1]

            for idx, character in enumerate(inputChars):
                pos = alphabet.find(character)
                number += pos * pow(alphabetLength, (len(data) - idx - 1))

        return number


def generate_id(id):
    return HashIDs().encrypt(id)


def verify_id(id):
    # return id  uncomment it for test_api.py work
    if id:
        id = HashIDs().decrypt(id)
        return id[0] if len(id) == 1 else -1
    return -1
