import React from 'react';

export default function NotFound() {
    return (
        <div className="error-container">
          <h1 className="error-heading">Oops! Something went wrong.</h1>
          <p className="error-message">
            We're sorry, but it seems there was an error. Please try again later.
          </p>
        </div>
      );
    };