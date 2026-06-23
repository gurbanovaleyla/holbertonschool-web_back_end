import { uploadPhoto, createUser } from "./utils.js";

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      const message = `${photo.body} ${user.firstName} ${user.lastName}`;
      console.log(message);
      return message;
    })
    .catch(() => {
      console.log("Signup system offline");
    });
}
