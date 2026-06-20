export default class Building {
  constructor(sqft) {
    this.sqft = sqft;

    if (this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }

  // abstract-like method (must be overridden)
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
