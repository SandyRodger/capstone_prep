# [Full stack open course](https://fullstackopen.com/en/)


## [part 3  - programming a server with NodeJS and Express](https://fullstackopen.com/en/part3)

### a

- run file as an npm script with `npm start`
- `npm test` except we don't have any tests right now.

- "These days, code that runs in the browser uses ES6 modules"
#### Simple web server

```index.js
const http = require('http')

const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' })
  response.end('Hello World')
})

const PORT = 3001
app.listen(PORT)
console.log(`Server running on port ${PORT}`)
```

#### Express

- We could implement the server on Node's built-in http web-server, but it's cumbersome. SO lots of libraries have been built to work with it. The most popular is Express.

`npm install express`

- the contents of the new `node_modules` directory are a list of all the new dependencies of the Express library. These are called the "transitive dependencies"

- the carent in: `"express": "^4.21.2"` is "semantic versioning" which means if and when the dependencies are updated the version of Express will be at least this version. THe first number will always be the same, but the last 2 might change.

- update dependencies with `npm update`
- install dependencies (like on another computer) with `npm install`
- newer versions of Express should be backwards compatible. So version `4.99.175` might work, but version `5.0.0` wouldn't.

#### Web and express

```
const express = require('express')
const app = express()

let notes = [
  ...
]

app.get('/', (request, response) => {
  response.send('<h1>Hello World!</h1>')
})

app.get('/api/notes', (request, response) => {
  response.json(notes)
})

const PORT = 3001
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})
```
- then restart (control c, node index.js)
- BUG -> I couldn't get my console to look like theirs:
  - I wasn't at the right url path
  - I didn't have the notes const in my file (their tutorial condensed that part)
  - then went to dev tools Network, clicked on `notes` and the panel reflected what it should have.

#### Automatic Change Tracking

- make the server track our changes with `node --watch index.js`
  - so we don't have to stop and reload our program each time
  - although you still have to reload the browser. That would be 'hot reload'ing and unlike React it's not possible here.
- change package.json to
```
{
  // ..
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  // ..
}
```
- and restart server with `npm run dev`
#### REST

- What REST is:
  - A style for building web APIs around resources (nouns)
  -  accessed over HTTP with standard methods.
  -  Keep servers stateless
  -  and use standard representations (usually JSON).

#### Fetching a single resource

- define parameters with colon syntax:

```index.js
app.get('/api/notes/:id', (request, response) => {
  const id = request.params.id
  const note = notes.find(note => note.id === id)
  response.json(note)
})
```

- problem now is that the server responds with `200 OK` even if the param doesn't exist.
- make the following change :

```index.js
app.get('/api/notes/:id', (request, response) => {
  const id = request.params.id
  const note = notes.find(note => note.id === id)
  

  if (note) {
    response.json(note)
  } else {
    response.status(404).end()
  }
})
```

#### Deleting resources

```
app.delete('/api/notes/:id', (request, response) => {
  const id = request.params.id
  notes = notes.filter(note => note.id !== id)

  response.status(204).end()
})
```

#### Postman

#### The Visual Studio Code REST client
- an alternative to Postman, so I'll skip.
- ok later I installed it. (It's an extension in VSCode).
- create `create_notes.rest`:
```
POST http"//localhost:3001/api/notes
Content-Type: application/json

{
  "content": "VS code rest client is a pre...",
  "important": true
}
```

<img width="1440" height="900" alt="Screenshot 2025-08-12 at 13 22 37" src="https://github.com/user-attachments/assets/e848805a-e1bf-4235-a749-ea19e680b5be" />

- One way the REST client is better than POSTMAN is you can save all your requests in the root of the project and they can be available to all of your team-mates
#### The WebStorm HTTP Client
- skip
#### Receiving data

- POST requests
- The Express json-parser : `app.use(express.json())`

```
const express = require('express')
const app = express()


app.use(express.json())

//...


app.post('/api/notes', (request, response) => {
  const note = request.body
  console.log(note)
  response.json(note)
})
```
- a potential bug is that the `content-type` header is misassigned. In which case the server can appear to only recieve an empty object.

###### important sidenote

- sometimes whern debugging you can find out what headers have been set in the HTTP request by using the get method of the request object. The `request` also has the headers property which contains all of the headers of a specific request
- If you leave a blank line between the top row and the row with the HTTP headers, i will be interpreted that there are not headers which caused a bug.
- You can spot the missing Content-Type header by doing `console.log(request.headers)` in your code. 

#### finalizing handling of request

```
app.post('/api/notes', (request, response) => {
  const maxId = notes.length > 0
    ? Math.max(...notes.map(n => Number(n.id))) 
    : 0

  const note = request.body
  note.id = String(maxId + 1)

  notes = notes.concat(note)

  response.json(note)
})
```

```
const generateId = () => {
  const maxId = notes.length > 0
    ? Math.max(...notes.map(n => Number(n.id)))
    : 0
  return String(maxId + 1)
}

app.post('/api/notes', (request, response) => {
  const body = request.body

  if (!body.content) {
    return response.status(400).json({ 
      error: 'content missing' 
    })
  }

  const note = {
    content: body.content,
    important: body.important || false,
    id: generateId(),
  }

  notes = notes.concat(note)

  response.json(note)
})
```

### Exercises:

###### 3.1

- `npm init`
- no changes to the input prompts
-  add "start": "node index.js" to the scripts block in my `package.json`
- `code .gitignore` with `node_modules` in line 1.
- change `index.js` to :
```
const http = require('http')

let contacts = [
    { 
      "id": "1",
      "name": "Arto Hellas", 
      "number": "040-123456"
    },
    { 
      "id": "2",
      "name": "Ada Lovelace", 
      "number": "39-44-5323523"
    },
    { 
      "id": "3",
      "name": "Dan Abramov", 
      "number": "12-43-234345"
    },
    { 
      "id": "4",
      "name": "Mary Poppendieck", 
      "number": "39-23-6423122"
    }
]

const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'application/json' })
  response.end(JSON.stringify(contacts))
})

const PORT = 3001
app.listen(PORT)
console.log(`server running on port ${PORT}`)
```

- `npm install express`
- `npm update`
- start with `node --watch index.js` so that changes are 

###### 3.2

```
const express = require('express')
const app = express()

let persons = [
    { 
      "id": "1",
      "name": "Arto Hellas", 
      "number": "040-123456"
    },
    { 
      "id": "2",
      "name": "Ada Lovelace", 
      "number": "39-44-5323523"
    },
    { 
      "id": "3",
      "name": "Dan Abramov", 
      "number": "12-43-234345"
    },
    { 
      "id": "4",
      "name": "Mary Poppendieck", 
      "number": "39-23-6423122"
    }
]

app.get('/', (request, response) => {
  response.send(`<h1>Hello World!</h1>`)
})

app.get('/api/persons', (request, response) => {
  response.json(persons)
})

app.get('/info', (request, response) => {
  const time = new Date()
  response.send(`
    <div>Phonebook has info for ${persons.length} people</div>
    <div>${time}</div>
    `)
})

const PORT = 3001
app.listen(PORT, () => {
  console.log(`server running on port ${PORT}`)
})
```

###### 3.3

```
const express = require('express')
const app = express()

let persons = [
  { 
    "id": "1",
    "name": "Arto Hellas", 
    "number": "040-123456"
  },
  { 
    "id": "2",
    "name": "Ada Lovelace", 
    "number": "39-44-5323523"
  },
  { 
    "id": "3",
    "name": "Dan Abramov", 
    "number": "12-43-234345"
  },
  { 
    "id": "4",
    "name": "Mary Poppendieck", 
    "number": "39-23-6423122"
  }
]

app.get('/', (request, response) => {
  response.send(`<h1>Hello World!</h1>`)
})

app.get('/api/persons', (request, response) => {
  response.json(persons)
})

app.get('/info', (request, response) => {
  const time = new Date()
  response.send(`
    <div>Phonebook has info for ${persons.length} people</div>
    <div>${time}</div>
    `)
})

app.get('/api/persons/:id', (request, response) => {
  const id = request.params.id
  const person = persons.find(person => person.id === id)

  if (person) {
    response.json(person)
  } else {
    response.status(404).end()
  }

  response.json(person)
})

const PORT = 3001
app.listen(PORT, () => {
  console.log(`server running on port ${PORT}`)
})
```

###### 3.4

```
const express = require('express')
const app = express()

let persons = [
  { 
    "id": "1",
    "name": "Arto Hellas", 
    "number": "040-123456"
  },
  { 
    "id": "2",
    "name": "Ada Lovelace", 
    "number": "39-44-5323523"
  },
  { 
    "id": "3",
    "name": "Dan Abramov", 
    "number": "12-43-234345"
  },
  { 
    "id": "4",
    "name": "Mary Poppendieck", 
    "number": "39-23-6423122"
  }
]

app.get('/', (request, response) => {
  response.send(`<h1>Hello World!</h1>`)
})

app.get('/api/persons', (request, response) => {
  response.json(persons)
})

app.get('/info', (request, response) => {
  const time = new Date()
  response.send(`
    <div>Phonebook has info for ${persons.length} people</div>
    <div>${time}</div>
    `)
})

app.get('/api/persons/:id', (request, response) => {
  const id = request.params.id
  const person = persons.find(person => person.id === id)

  if (person) {
    response.json(person)
  } else {
    response.status(404).end()
  }

  response.json(person)
})

app.delete('/api/persons/:id', (request, response) => {
  const id = request.params.id
  persons = persons.filter(note => note.id !== id)

  response.status(204).end()
})

const PORT = 3001
app.listen(PORT, () => {
  console.log(`server running on port ${PORT}`)
})
```

##### 3.5

- (I thought I might have to use the REST extention and create a requests folder, but in the end no.)
```
app.post('/api/persons', (request, response) => {

  if (!request.body) {
    return response.status(400).json({
      error: 'content missing'
    })
  }

  const person = {
    content: request.body,
    important: request.body.important || false,
    id: String(Math.floor(Math.random() * 1000000))
  }

  response.json(person)
})
```
##### 3.6

```
  if (!request.body.name) {
    return response.status(400).json({
      error: 'name missing'
    })
  } else if (!request.body.number) {
      return response.status(400).json({
      error: 'number missing'
  })
  } else if ((persons.filter(p => p.name ===request.body.name)).length) {
    return response.status(400).json({
    error: `name must be unique`
  })
}
```

### About HTTP request types

- requests should be "safe"
  - no side-effects
- all HTTP requests apart from POST should be idempotent.

### Middleware

- like the json-parser we used earlier. It takes the raw data from the request, parses it into an object and assigns it to the request object as a new body.
- Wyen you have multiple middlewares they are executed successively in the order they're written in the application code.
- We will now implemenet a middleware that prints information about every request sent to the server.

```
const requestLogger = (request, response, next) => {
  console.log('Method:', request.method)
  console.log('Path:  ', request.path)
  console.log('Body:  ', request.body)
  console.log('---')
  next()
}
```

```
app.use(requestLogger)
```

```
const unknownEndpoint = (request, response) => {
  response.status(404).send({ error: 'unknown endpoint' })
}

app.use(unknownEndpoint)
```

###### 3.7

`npm install morgan`
`const morgan = require('morgan')
`app.use(morgan('tiny'))`

###### 3.8

```
morgan.token('body', (req) => {
  return JSON.stringify(req.body)
})

app.use(morgan(':method :url :status :res[content-length] - :response-time ms :body'))
```
