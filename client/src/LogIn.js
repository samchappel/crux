import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const initialValuesSignUp = {
  username: '',
  email: '',
  password: '',
  firstName: '',
  lastName: '',
};

const signUpValidationSchema = Yup.object().shape({
  username: Yup.string()
    .min(3, 'Must be at least 3 characters')
    .test('unique-username', 'This username is already taken', async (value) => {
      const response = await fetch(`/check-username?username=${value}`);
      const data = await response.json();
      return data.isUnique;
    })
    .required('Required'),
  email: Yup.string()
    .email('Invalid email')
    .test('unique-email', 'This email is already taken', async (value) => {
      const response = await fetch(`/check-email?email=${value}`);
      const data = await response.json();
      return data.isUnique;
    })
    .required('Required'),
  password: Yup.string()
    .min(8, 'Must be at least 8 characters')
    .matches(/[!@#$%^&*]/, 'Must contain a special character')
    .required('Required'),
  firstName: Yup.string().required('Required'),
  lastName: Yup.string().required('Required'),
});

function LogIn() {
  const history = useHistory();
  const [showSignUp, setShowSignUp] = useState(false);

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

  const handleSignUp = async (values, actions) => {
    try {
      const response = await fetch('/signup', {
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
        actions.setFieldError('general', 'Sign-up failed');
      }
    } catch (error) {
      actions.setSubmitting(false);
      actions.setFieldError('general', 'An error occurred. Please try again.');
    }
  };

  const toggleSignUp = () => {
    setShowSignUp(prevState => !prevState);
  }

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
                <Field type="username" name="username" placeholder="Username" />
                <ErrorMessage name="username" />
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
    
        <hr />
    
        <p>NEED TO SIGN UP? CLICK HERE!</p>
  <button onClick={() => setShowSignUp(!showSignUp)}>
    {showSignUp ? 'Hide Sign Up' : 'Show Sign Up'}
  </button>
  {showSignUp && (
    <Formik
      initialValues={initialValuesSignUp}
      validationSchema={signUpValidationSchema}
      onSubmit={handleSignUp}
    >
      {({ isSubmitting }) => (
        <Form>
          <div>
            <Field type="text" name="username" placeholder="Username" />
            <ErrorMessage name="username" />
          </div>
          <div>
            <Field type="email" name="email" placeholder="Email" />
            <ErrorMessage name="email" />
          </div>
          <div>
            <Field type="password" name="password" placeholder="Password" />
            <ErrorMessage name="password" />
          </div>
          <div>
            <Field type="text" name="firstName" placeholder="First Name" />
            <ErrorMessage name="firstName" />
          </div>
          <div>
            <Field type="text" name="lastName" placeholder="Last Name" />
            <ErrorMessage name="lastName" />
          </div>
          <button type="submit" disabled={isSubmitting}>
            Sign Up
          </button>
          <ErrorMessage name="general" />
        </Form>
      )}
    </Formik>
  )}
</div>
    );
}

export default LogIn;

