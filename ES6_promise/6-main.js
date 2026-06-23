import handleProfileSignup from './6-final-user';

handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg').then((response) => {
  console.log(response);
});
