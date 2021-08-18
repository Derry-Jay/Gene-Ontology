export class User {
  constructor (name, date, type, gender, mobile, email, latitude, longitude, bloodType, rhesusProteinStatus) {
    this.name = name
    this.date = Date(date)
    this.type = type
    this.gender = gender
    this.mobile = mobile
    this.email = email
    this.latitude = latitude
    this.longitude = longitude
    this.bloodType = bloodType
    this.rhesusProteinStatus = rhesusProteinStatus
  }

  fromJSON (json) {
    User(json.name, json.date, json.type, json.gender, json.mobile, json.email, json.latitude, json.longitude, json.bloodType, json.rhesusProteinStatus)
  }
}
export default {
  User
}
