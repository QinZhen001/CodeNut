import storage from 'good-storage'

const SEARCH_KEY = '__search__'
const SEARCH_MAX_LEN = 15

const PLAY_KEY = '__play__'
const PLAY_MAX_LEN = 200

const FAVORITE_KEY = '__favorite__'
const FAVORITE_MAX_LEN = 200

const TOKEN_KEY = '__token__'
const ID_KEY = '__id__'

function insertArray(arr, val, compare, maxLen) {
  const index = arr.findIndex(compare)
  if (index === 0) {
    return
  }
  if (index > 0) {
    arr.splice(index, 1)
  }
  arr.unshift(val)
  if (maxLen && arr.length > maxLen) {
    arr.pop()
  }
}

function deleteFromArray(arr, compare) {
  const index = arr.findIndex(compare)
  if (index > -1) {
    arr.splice(index, 1)
  }
}

export function saveSearch(query) {
  let searches = storage.get(SEARCH_KEY, [])
  insertArray(searches, query, (item) => {
    return item === query
  }, SEARCH_MAX_LEN)
  storage.set(SEARCH_KEY, searches)
  return searches
}

export function deleteSearch(query) {
  let searches = storage.get(SEARCH_KEY, [])
  deleteFromArray(searches, (item) => {
    return item === query
  })
  storage.set(SEARCH_KEY, searches)
  return searches
}

export function clearSearch() {
  storage.remove(SEARCH_KEY)
  return []
}

export function loadSearch() {
  return storage.get(SEARCH_KEY, [])
}

export function savePlay(song) {
  let songs = storage.get(PLAY_KEY, [])
  insertArray(songs, song, (item) => {
    return song.id === item.id
  }, PLAY_MAX_LEN)
  storage.set(PLAY_KEY, songs)
  return songs
}

export function loadPlay() {
  return storage.get(PLAY_KEY, [])
}

export function saveFavorite(problem) {
  let problems = storage.get(FAVORITE_KEY, [])
  insertArray(problems, problem, (item) => {
    return problem.id === item.id
  }, FAVORITE_MAX_LEN)
  storage.set(FAVORITE_KEY, problems)
  return problems
}

export function deleteFavorite(problem) {
  let problems = storage.get(FAVORITE_KEY, [])
  deleteFromArray(problems, (item) => {
    return item.id === problem.id
  })
  storage.set(FAVORITE_KEY, problems)
  return problems
}

export function loadFavorite() {
  return storage.get(FAVORITE_KEY, [])
}

export function saveToken (token) {
  storage.set(TOKEN_KEY, token)
}

export function getToken () {
  return storage.get(TOKEN_KEY, '')
}

export function clearToken () {
  storage.remove(TOKEN_KEY)
}

export function saveUserId (id) {
  storage.set(ID_KEY, id)
}

export function getUserId () {
  return storage.get(ID_KEY, '')
}

export function clearUserId () {
  storage.remove(ID_KEY)
}