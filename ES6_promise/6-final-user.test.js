import handleProfileSignup from './6-final-user';

describe('handleProfileSignup', () => {
  it('returns an array of settled promise results', async () => {
    expect.assertions(2);
    const result = await handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg');

    expect(Array.isArray(result)).toBe(true);
    expect(result).toHaveLength(2);
  });

  it('first result is the fulfilled signUpUser result', async () => {
    expect.assertions(2);
    const result = await handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg');

    expect(result[0].status).toBe('fulfilled');
    expect(result[0].value).toStrictEqual({
      firstName: 'Bob',
      lastName: 'Dylan',
    });
  });

  it('second result is the rejected uploadPhoto result', async () => {
    expect.assertions(3);
    const result = await handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg');

    expect(result[1].status).toBe('rejected');
    expect(result[1].value).toBeInstanceOf(Error);
    expect(result[1].value.message).toBe('bob_dylan.jpg cannot be processed');
  });
});
