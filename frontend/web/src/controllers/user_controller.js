import router from '../router'
import login from '../repos/user_repos'
export class UserController {
  constructor () {
    console.info('Hi')
  }

  async login (params) {
    var lgd = await login(params)
    if (lgd.success && lgd.status) {
      const passData = { 'name': 'Home' }
      router.push(passData)
    }
  }
}

export default {
  UserController
}
