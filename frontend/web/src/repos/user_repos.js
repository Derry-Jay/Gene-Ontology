import router from '../router'
import User from '../models/user'
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
    this.data = data
    console.log(this.data)
    if (data.success && data.status) {
      const passData = { 'name': 'Home' }
      router.push(passData)
    } else {
      console.log('hi')
    }
  } else {
    console.log('bye')
  }
}
