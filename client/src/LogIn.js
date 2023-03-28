import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

function LogIn() {
  const history = useHistory();

  const initialValues = {
    email: '',
    password: '',
  };

  const validationSchema = Yup.object().shape({
    email: Yup.string().email('Invalid email').required('Required'),
    password: Yup.string().required('Required'),
  });

  const handleLogin = async (values, actions) => {
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });
  
      if (response.ok) {
        const climber = await response.json();
        localStorage.setItem('climber', JSON.stringify(climber));
        history.push('/profile');
      } else {
        actions.setSubmitting(false);
        actions.setFieldError('general', 'Login failed');
      }
    } catch (error) {
      actions.setSubmitting(false);
      actions.setFieldError('general', 'An error occurred. Please try again.');
    }
  };

  return (
    <div>
      <p>LOG IN</p>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleLogin}
      >
        {({ isSubmitting }) => (
          <Form>
            <div>
              <Field type="email" name="email" placeholder="Email" />
              <ErrorMessage name="email" />
            </div>
            <div>
              <Field type="password" name="password" placeholder="Password" />
              <ErrorMessage name="password" />
            </div>
            <button type="submit" disabled={isSubmitting}>
              Log In
            </button>
            <ErrorMessage name="general" />
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default LogIn;