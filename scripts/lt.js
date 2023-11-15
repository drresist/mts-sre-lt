import http from 'k6/http';

export default function () {
  const url = 'http://91.185.85.213/weatherforecast'

  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Host' : "sre-course-102"
    },
  };

  http.get(url, params);
}
