/**
 * Custom Error class, JSON conversion function, status code, response message
 *
 * @author seu0313
 * @since 2.0.0
 */

// custom Error class
export class resError extends Error {
  success: boolean = false;
  status: number;
  data?: any;

  constructor(status: number, message: string, data?: any) {
    super(message);
    this.status = status;
    this.data = data;
  }
}

// custom JSON conversion function
export const resJSON = (
  success: boolean = true,
  message: string,
  data?: any
) => {
  return {
    success,
    message,
    data,
  };
};

// status code, custom response message
export const status = {
  // status code
  OK: 200,
  CREATED: 201,
  NO_CONTENT: 204,
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  INTERNAL_SERVER_ERROR: 500,
  SERVICE_UNAVAILABLE: 503,
  DB_ERROR: 600,
};

export const resMSG = {
  // status code messages
  OK: "Ok",
  CREATED: "Created",
  NO_CONTENT: "No Content",
  BAD_REQUEST: "Bad Request",
  UNAUTHORIZED: "Unauthorized",
  FORBIDDEN: "Forbidden",
  NOT_FOUND: "Not Found",
  INTERNAL_SERVER_ERROR: "Internal Server Error",
  SERVICE_UNAVAILABLE: "Service Unavailable",
  DB_SUCCESS: "DB Access Success",
  DB_ERROR: "DB Access Fail",
};
