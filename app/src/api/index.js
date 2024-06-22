export const BASE_URL = "127.0.0.1:8080"

/**
 * A generic wrapper function for making HTTP requests using the Fetch API.
 * @param {Object} options - The configuration options for the HTTP request.
 * @param {string} options.url - The URL to which the request is sent.
 * @param {string} [options.method='GET'] - The HTTP method to use for the request (GET, POST, PUT, DELETE, etc.).
 * @param {Object|null} [options.body=null] - The body of the request, typically used with POST, PUT, or PATCH requests.
 * @param {Object|null} [options.param=null] - Query parameters to append to the URL.
 * @param {Object|null} [options.headers=null] - Custom headers to include in the request.
 *
 * @returns {Promise<Object>} A promise that resolves to an object containing the status code and response data.
 * @returns {number|null} return.statusCode - The HTTP status code of the response. Null if the request fails.
 * @returns {Object|null} return.responseData - The JSON-parsed response data. Null if the request fails or if the response contains no JSON data.
 *
 * @example
 * // Example usage:
 * const response = await fetchData({
 *   url: 'https://api.example.com/data',
 *   method: 'POST',
 *   body: { key: 'value' },
 *   headers: { 'Authorization': 'Bearer token' }
 * });
 *
 * if (response.statusCode === 200) {
 *   console.log('Data:', response.responseData);
 * } else {
 *   console.error('Error:', response.statusCode);
 * }
 */
export const fetchData = async ({
                                    url,
                                    method = 'GET',
                                    body = null,
                                    param = null,
                                    headers = null
                                }) => {

    let requestInfo = {
        method,
        headers: {
            'Content-Type': 'application/json' // Set content type for JSON data
        }
    };

    if (headers) {
        requestInfo.headers = headers;
    }

    if (body) {
        Object.defineProperty(requestInfo, 'body', {
            value: JSON.stringify(body),
            writable: true
        });
    }

    let urlWithParams;

    if (param) {
        const encodedParams = Object.keys(param).map(key =>
            `${encodeURIComponent(key)}=${encodeURIComponent(param[key])}`).join('&');
        urlWithParams = `${url}?${encodedParams}`;
    }


    try {
        const request = await fetch(urlWithParams ?? url, requestInfo);
        const response = await request;
        let jsonRes = null;

        try {
            jsonRes = await response.json();
        } catch (jsonError) {
            console.log('No JSON data:', jsonError.message);
        }

        return {
            statusCode: response.status,
            responseData: jsonRes
        };

    } catch (fetchError) {
        console.error('Fetch error:', fetchError.message);
        return {
            statusCode: null,
            responseData: null
        };
    }
};