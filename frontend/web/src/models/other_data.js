export class OtherData {
  constructor (success, status, message) {
    this.success = success
    this.status = status
    this.message = message
  }

  fromJSON (json) {
    OtherData(json.success, json.status, json.message)
  }
}
export default {
  OtherData
}
