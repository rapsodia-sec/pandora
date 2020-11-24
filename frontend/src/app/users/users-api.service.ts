import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import {API_URL} from '../env';
import {User} from './user.model';

@Injectable()
export class UsersApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getUsers(): any{
    return this.http
      .get(`${API_URL}/users`).pipe(
        map(data => {
          return data;
        }),
        // "catchError" instead "catch
        catchError(error => {
          return UsersApiService._handleError(error);
        })
      );
  }
}
