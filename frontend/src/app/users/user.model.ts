export class User {
  constructor(
    public username: string,
    public fname: string,
    public lname: string,
    public email: string,
    public passwordhash: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string,
  ) { }
}
