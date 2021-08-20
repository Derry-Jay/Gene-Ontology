import { User } from '../models/user'
import { OtherData } from '../models/other_data'
async function login (json) {
  const request = new Request('http://localhost:8000/login', {
    method: 'POST',
    mode: 'cors',
    cache: 'default',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(json)
  })
  const res = await fetch(request)
  if (res.ok) {
    const data = await res.json()
    this.data = OtherData.fromJSON(data.result)
    console.log(data)
    if (data.success && data.status) {
      return this.data
    } else {
      console.log('hi')
    }
  } else {
    console.log('bye')
  }
}
async function getUserDetails (params) {
  try {
    const request = new Request('http://localhost:8000/userDetails', {
      method: 'POST',
      mode: 'cors',
      cache: 'default',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(params)
    })
    const res = await fetch(request)
    if (res.ok) {
      const data = await res.json()
      this.data = User.fromJSON(data.result)
      console.log(data)
      if (data.success && data.status) {
        return this.data
      } else {
        console.log('Hi')
      }
    } else {
      console.log('Wait')
    }
  } catch (e) {
    console.log('Bye')
    throw e
  }
}
export default {
  login,
  getUserDetails
}
