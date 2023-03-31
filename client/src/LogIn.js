import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import Modal from 'react-modal';

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
    username: '',
    password: '',
  };

  const validationSchema = Yup.object().shape({
    username: Yup.string()
      .min(3, 'Must be at least 3 characters')
      .required('Required'),
    password: Yup.string()
      .required('Required'),
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
        sessionStorage.setItem('climber', JSON.stringify(climber));
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
        //need to update this from localstorage
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
      <h2 className='login-title'>LOG IN</h2>
      <Formik
        initialValues={initialValues}
        onSubmit={handleLogin}
        validationSchema={validationSchema}
        >
        {props => (
          <Form onSubmit={props.handleSubmit}>
            <div>
            <Field
              type="text"
              name="username"
              placeholder="Username"
              onChange={props.handleChange}
              onBlur={props.handleBlur}
              value={props.values.username}
            />
              {props.errors.username && <div id="feedback">{props.errors.username}</div>}
            </div>
            <div>
              <Field
                type="password"
                name="password"
                placeholder="Password"
                onChange={props.handleChange}
                onBlur={props.handleBlur}
                value={props.values.password}
              />
              {props.errors.password && <div id="feedback">{props.errors.password}</div>}
            </div>
            <button type="submit" disabled={props.isSubmitting}>
              Log In
            </button>
            <button type="button" onClick={toggleSignUp}>
              Create Account
            </button>
            {props.errors.general && <div id="feedback">{props.errors.general}</div>}
          </Form>
        )}
        </Formik>
        {showSignUp && (
          <div className="modal">
            <div className="modal-content">
              <button className="close-button" onClick={toggleSignUp}>
                X
              </button>
              <h2>Create an Account</h2>
              <Formik
                initialValues={initialValuesSignUp}
                validationSchema={signUpValidationSchema}
                onSubmit={handleSignUp}
              >
                {props => (
                  <Form onSubmit={props.handleSubmit}>
                    <div>
                      <Field
                        type="username"
                        name="username"
                        placeholder="Username"
                        onChange={props.handleChange}
                        onBlur={props.handleBlur}
                        value={props.values.username}
                      />
                      {props.errors.username && <div id="feedback">{props.errors.username}</div>}
                    </div>
                    <div>
                      <Field
                        type="email"
                        name="email"
                        placeholder="Email"
                        onChange={props.handleChange}
                        onBlur={props.handleBlur}
                        value={props.values.email}
                      />
                      {props.errors.email && <div id="feedback">{props.errors.email}</div>}
                    </div>
                    <div>
                      <Field
                        type="password"
                        name="password"
                        placeholder="Password"
                        onChange={props.handleChange}
                        onBlur={props.handleBlur}
                        value={props.values.password}
                      />
                      {props.errors.password && <div id="feedback">{props.errors.password}</div>}
                    </div>
                    <div>
                      <Field
                        type="firstName"
                        name="firstName"
                        placeholder="First Name"
                        onChange={props.handleChange}
                        onBlur={props.handleBlur}
                        value={props.values.firstName}
                      />
                      {props.errors.firstName && <div id="feedback">{props.errors.firstName}</div>}
                    </div>
                    <div>
                      <Field
                        type="lastName"
                        name="lastName"
                        placeholder="Last Name"
                        onChange={props.handleChange}
                        onBlur={props.handleBlur}
                        value={props.values.lastName}
                      />
                      {props.errors.lastName && <div id="feedback">{props.errors.lastName}</div>}
                    </div>
                    <button type="submit" disabled={props.isSubmitting}>
                      Create Account
                    </button>
                    <button type="button" onClick={toggleSignUp}>
                      Cancel
                    </button>
                    {props.errors.general && <div id="feedback">{props.errors.general}</div>}
                  </Form>
                )}
              </Formik>
            </div>
          </div>
        )}
        </div>
  )
}

export default LogIn;