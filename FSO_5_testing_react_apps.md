# [testing react apps](https://fullstackopen.com/en/part5)

## [a login front end](https://fullstackopen.com/en/part5/login_in_frontend)

### Handling login
```
{user === null && loginForm()}
{user !== null && noteForm()}
```
equivalent to

```
    {user === null ?
      loginForm() :
      noteForm()
    }

```
### Creating new notes
- creating a new note involves an authorization token now:
```
import axios from 'axios'
const baseUrl = '/api/notes'


let token = null


const setToken = newToken => {
  token = `Bearer ${newToken}`
}

const getAll = () => {
  const request = axios.get(baseUrl)
  return request.then(response => response.data)
}


const create = async newObject => {
  const config = {
    headers: { Authorization: token },
  }


  const response = await axios.post(baseUrl, newObject, config)
  return response.data
}

const update = (id, newObject) => {
  const request = axios.put(`${ baseUrl }/${id}`, newObject)
  return request.then(response => response.data)
}


export default { getAll, create, update, setToken }
```

### Saving the token to the browser's local storage
- Local Storage is a key-value database in the browser.

```
      window.localStorage.setItem(
        'loggedNoteappUser', JSON.stringify(user)
      )
```

```
  useEffect(() => {
    const loggedUserJSON = window.localStorage.getItem('loggedNoteappUser')
    if (loggedUserJSON) {
      const user = JSON.parse(loggedUserJSON)
      setUser(user)
      noteService.setToken(user.token)
    }
  }, [])
```

`window.localStorage.removeItem('loggedNoteappUser')`
`window.localStorage.clear()`
### Exercises 5.1 - 5.4
- skip for now
### ESlint
### 5.12
### A note on using local storage
- There are two solutions to the problem. The first one is to limit the validity period of a token. This forces the user to re-login to the app once the token has expired. The other approach is to save the validity information of each token to the backend database. This solution is often called a server-side session.
## [b props.children and proptypes](https://fullstackopen.com/en/part5/props_children_and_proptypes)

### Displaying the login form only when appropriate
### The components children, aka. props.children
### State of the forms

- Sometimes, you want the state of two components to always change together. To do it, remove state from both of them, move it to their closest common parent, and then pass it down to them via props. This is known as lifting state up, and it’s one of the most common things you will do writing React code.
### References to components with ref
- The component uses the useImperativeHandle hook to make its toggleVisibility function available outside of the component.
### One point about components
### Exercises 5.5 - 5.11
### PropTypes
## [c testing react apps](https://fullstackopen.com/en/part5/testing_react_apps)
- vitest
- jsdom
### Rendering the component for tests
### Test file location
### Searching for content in a component
### Debugging tests
### Clicking buttons in tests
### Tests for the Togglable component
### Testing the forms
### About finding the elements
### Test coverage
### Exercises 5.12 - 5.16
### Frontend integration tests
### Snapshot testing
## [d end to end testing: playwright](https://fullstackopen.com/en/part5/end_to_end_testing_playwright)
### Playwright
### Initializing tests
### Testing our own code
### Testing note creation
### Controlling the state of the database
### Test for failed login
### Running tests one by one
### Helper functions for tests
### Note importance change revisited
### Test development and debugging
### exercises 5.17 - 5.23
## [e end to end testing: Cypress](https://fullstackopen.com/en/part5/end_to_end_testing_cypress)
### Cypress
### Writing to a form
### Testing new note form
### Controlling the state of the database
### Failed login test
### Bypassing the UI
### Changing the importance of a note
### Running and debugging the tests
### 5.17 - 5.23
