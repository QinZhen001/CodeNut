export function formatDate (date, fmt) {
  if (/(y+)/.test(fmt)) {
    fmt = fmt.replace(RegExp.$1, (date.getFullYear() + '').substr(4 - RegExp.$1.length))
  }
  let o = {
    'M+': date.getMonth() + 1,
    'd+': date.getDate(),
    'h+': date.getHours(),
    'm+': date.getMinutes(),
    's+': date.getSeconds()
  }
  for (let k in o) {
    if (new RegExp(`(${k})`).test(fmt)) {
      let str = o[k] + ''
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? str : padLeftZero(str))
    }
  }
  return fmt
}

function padLeftZero (str) {
  return ('00' + str).substr(str.length)
}

export function getAbsPosition (element) {
  let abs = {x: 0, y: 0}// 如果浏览器兼容此方法
  if (document.documentElement.getBoundingClientRect) {
    // 注意，getBoundingClientRect()是jQuery对象的方法
    // 如果不用jQuery对象，可以使用else分支。
    abs.x = element.getBoundingClientRect().left
    abs.y = element.getBoundingClientRect().top
  } else {
    // 如果浏览器不兼容此方法
    while (element !== document.body) {
      abs.x += element.offsetLeft
      abs.y += element.offsetTop
      element = element.offsetParent
    }
  }
  return abs
}

export function RandomNumBoth (Min, Max) {
  var Range = Max - Min
  var Rand = Math.random()
  var num = Min + Math.round(Rand * Range)//四舍五入
  return num
}

