import axios from 'axios'
import { getToken } from 'common/js/cache'

export function clearAxiosInterceptor () {
  axios.interceptors.request.use(
    config => {
      config.headers.token = ''
      config.auth = {}
      return config
    },
    err => {
      return Promise.reject(err)
    })
}

export function changeAxiosInterceptor (username, password) {
  axios.interceptors.request.use(
    config => {
      config.headers.token = getToken()
      config.auth = {
        username: username,
        password: password
      }
      return config
    },
    err => {
      return Promise.reject(err)
    })
}
