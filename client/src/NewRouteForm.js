import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const initialValues = {
  name: '',
  grade: '',
  location: '',
  image: '',
  style: '',
  review: '',
};

const validationSchema = Yup.object().shape({
  name: Yup.string().required('Required'),
  grade: Yup.string().required('Required'),
  location: Yup.string().required('Required'),
  image: Yup.string().url('Invalid URL').required('Required'),
  style: Yup.string().required('Required'),
  review: Yup.string().required('Required'),
});

const onSubmit = (values, { setSubmitting }) => {
  setTimeout(() => {
    alert(JSON.stringify(values, null, 2));
    setSubmitting(false);
  }, 400);
};

const NewRouteForm = () => (
  <div id="form-wrapper">
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={onSubmit}
    >
      {({ isSubmitting }) => (
        <Form id="route-form">
          <h2 id="submit-title">Submit a New Route</h2>

          <label htmlFor="form-name">Route Name:</label>
          <Field type="text" id="form-name" name="name" />

          <ErrorMessage name="name" />

          <label htmlFor="form-grade">Route Grade:</label>
          <Field type="text" id="form-grade" name="grade" />

          <ErrorMessage name="grade" />

          <label htmlFor="form-location">Location:</label>
          <Field type="text" id="form-location" name="location" />

          <ErrorMessage name="location" />

          <label htmlFor="form-image">Image URL:</label>
          <Field type="text" id="form-image" name="image" />

          <ErrorMessage name="image" />

          <label htmlFor="form-style">Route Style:</label>
          <Field type="text" id="form-style" name="style" />

          <ErrorMessage name="style" />

          <label htmlFor="form-review">Review:</label>
          <Field type="text" id="form-review" name="review" />

          <ErrorMessage name="review" />

          <button type="submit" disabled={isSubmitting}>
            Submit
          </button>
        </Form>
      )}
    </Formik>
  </div>
);

export default NewRouteForm;