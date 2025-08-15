# [Full stack open course]([https://fullstackopen.com/en/](https://fullstackopen.com/en/part2))

### code for staring a new project

- `npm create vite@latest 02_exercises -- --template react` in an empty directory
- `npm install`
- `npm run dev`

## [a => Rendering a collection, modules](https://fullstackopen.com/en/part2/rendering_a_collection_modules)
### console.log
- experienced developers use it 10x more.
- and do this: `console.log('props value is', props)` instead of using a `+`.
### Protip: Visual Studio Code snippets
- shortcuts for quickly generating commonly re-used portions of code:
- [official instructions](https://code.visualstudio.com/docs/editing/userdefinedsnippets#_creating-your-own-snippets)
- Code > Settings > select langauge, then:
```
{
  "cheeky_snip_snip": {
    "prefix": ["sandy", "snippet"], <= the words that will trigger the snippet suggestion
    "body": ["(function sandySnip() { console.log('you gash-strumpet')})()"], <= the code
    "description": "pretty important" 
  }
```

### JavaScript Arrays
- if you don't know how to do this watch these videos, blah blah blah
### Event Handlers Revisited
- this is tough for many students (but I'm going to press on because I did Launch School)
### Rendering Collections
- ok so we transform an array with map, into 3 `<li>`s instead of writing each one out in HTML:
```
      <ul>
        {notes.map(note => 
          <li>{note.content}</li>
        )}
      </ul>
```
### Key-attribute
- warning in the console: `Each child in a list should have a unique "key" prop.`
  - so we add a key : `          <li key={note.id}>`
### Map
- skim
### Anti-pattern: Array Indexes as Keys
- potential bug if you use the array indexes as keys
### Refactoring Modules
- create `Notes` :

```
const Note = ({note}) => {
  return (
    <li>{note.content}</li>
  )
}
```

- common practice is to make each module its own file, like the two first lines:

```
import ReactDOM from "react-dom/client"
import App from "./App"
```
- In smaller applications components are placed in a directory called 'components'
- which is what we do at this step:
`mkdir components`
`code Note.jsx`
```
const Note = ({ note }) => {
  return <li>{note.content}</li>
}

export default Note
```
- and import it elsewhere:
`import Note from './components/Note'`

### When the Application Breaks
- debugging walkthrough
- console.log your way out....
### Web developer's oath
- rules:
  - I will have my browser developer console open all the time
  - I progress with small steps
  - I will write lots of console.log statements to make sure I understand how the code behaves and to help pinpoint problems
  - If my code does not work, I will not write more code. Instead, I start deleting the code until it works or just return to a state when everything was still working
When I ask for help in the course Discord channel or elsewhere I formulate my questions properly, see here how to ask for help

#### Final forms:

```App.jsx
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Note from './components/Note'
import './App.css'

const App = ({notes}) => {
  return (
    <div>
      <h1>Notes</h1>
      <ul>
        {notes.map(note => 
          <Note key={note.id} note={note} />
        )}
      </ul>
    </div>
  )
}

export default App
```

```main.jsx
import ReactDOM from 'react-dom/client'
import App from './App'

const notes = [
  {
    id: 1,
    content: 'HTML is easy',
    important: true
  },
  {
    id: 2,
    content: 'Browser can execute only JavaScript',
    important: false
  },
  {
    id: 3,
    content: 'GET and POST are the most important methods of HTTP protocol',
    important: true
  }
]

ReactDOM.createRoot(document.getElementById('root')).render(
  <App notes={notes} />
)
```
### Exercises:

- `npm create vite@latest 02_exercises -- --template react` in an empty directory
- `npm install`
- `npm run dev`
  
#### 2.1

```components/course.jsx
const Course = ({ course }) => {
  return <>
      <h1>{course.name}</h1>
      {course.parts.map(p => <div key={p.id}>{p.name} : {p.exercises} exercises</div>)}
    </>
}

export default Course
```

```app.jsx
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Course from './components/Course'
import './App.css'

const App = () => {
  const course = {
    id: 1,
    name: 'Half Stack application development',
    parts: [
      {
        name: 'Fundamentals of React',
        exercises: 10,
        id: 1
      },
      {
        name: 'Using props to pass data',
        exercises: 7,
        id: 2
      },
      {
        name: 'State of a component',
        exercises: 14,
        id: 3
      }
    ]
  }

  return <Course course={course} />
}

export default App
```

#### 2.2

`<div>total of {course.parts.map(p => p.exercises).reduce((a, v) => a + v)} exercises</div>`

#### 2.3

- as above

#### 2.4

```
import { useState } from 'react'
import './App.css'

const Course = (course) => {
  return <>
    <h2>{course.name}</h2>
    {course.parts.map(p => <div>{p.name} {p.exercises}</div>)}
    <h3>total of {course.parts.map(c => c.exercises).reduce((a, v) => a + v)} exercises</h3>
  </>
}

const Courses = ({ courses }) => {
  return <>
    <h1>Web development curriculum</h1>
    {courses.map(c => Course(c))}
  </>
}

const App = () => {
  const courses = [
    {
      name: 'Half Stack application development',
      id: 1,
      parts: [
        {
          name: 'Fundamentals of React',
          exercises: 10,
          id: 1
        },
        {
          name: 'Using props to pass data',
          exercises: 7,
          id: 2
        },
        {
          name: 'State of a component',
          exercises: 14,
          id: 3
        },
        {
          name: 'Redux',
          exercises: 11,
          id: 4
        }
      ]
    }, 
    {
      name: 'Node.js',
      id: 2,
      parts: [
        {
          name: 'Routing',
          exercises: 3,
          id: 1
        },
        {
          name: 'Middlewares',
          exercises: 7,
          id: 2
        }
      ]
    }
  ]

  return <Courses courses={courses} />
}

export default App
```

#### 2.5

```App.jsx
import { useState } from 'react'
import './App.css'
import Courses from './components/Courses'

const App = () => {
  const courses = [
    {
      name: 'Half Stack application development',
      id: 1,
      parts: [
        {
          name: 'Fundamentals of React',
          exercises: 10,
          id: 1
        },
        {
          name: 'Using props to pass data',
          exercises: 7,
          id: 2
        },
        {
          name: 'State of a component',
          exercises: 14,
          id: 3
        },
        {
          name: 'Redux',
          exercises: 11,
          id: 4
        }
      ]
    }, 
    {
      name: 'Node.js',
      id: 2,
      parts: [
        {
          name: 'Routing',
          exercises: 3,
          id: 1
        },
        {
          name: 'Middlewares',
          exercises: 7,
          id: 2
        }
      ]
    }
  ]

  return <Courses courses={courses} />
}

export default App
```

```Courses.jsx
const Course = (course) => {
  return <>
    <h2>{course.name}</h2>
    {course.parts.map(p => <div>{p.name} {p.exercises}</div>)}
    <h3>total of {course.parts.map(c => c.exercises).reduce((a, v) => a + v)} exercises</h3>
  </>
}

const Courses = ({ courses }) => {
  return <>
    <h1>Web development curriculum</h1>
    {courses.map(c => Course(c))}
  </>
}

export default Courses
```

## [b => Forms](https://fullstackopen.com/en/part2/forms)

- recreate project from part a, because I wrote over it:
  - `npm create vite@latest 02b_forms -- --template react` in `/Users/sandyboy/Desktop/capstone_prep/01_fullstack_open_course`
  - `npm install`
  - `npm run dev`

  - hmmm, why does my directory lack files that are in the model directory (https://github.com/fullstack-hy2020/part2-notes-frontend/tree/part2-1)
    - I will copy them in:
      - `vite.config.js`
      - `package.json`
      - `package-lock.json`
      - `index.html`
      - `eslint.config.js`
      - `README.md`
      - `.gitignore`
- remove:
  - `App.css`
  - `index.css`
  - `assets` directory
- That was a ball-ache-> next time just pull the directory

### Saving the notes in the component state
- more `useState()`
- Add a form:

```
  const addNote = (event) => {
    event.preventDefault()
    console.log('button clicked', event.target)
  }
```

```
  <form onSubmit={addNote}>
    <input />
    <button type="submit">save</button>
  </form>
```
### Controlled component

- How to access the data in the input element

```
  const [newNote, setNewNote] = useState(
    'a new note...'
  )
```

- we use the `onChange` event meaning it registers every time there is a change in the input
```
<input
  value={newNote}
  onChange={handleNoteChange}
/>
```

- Add React dev tools (Which i was meant to already have done, somehow)
  - https://react.dev/learn/preserving-and-resetting-state#option-2-resetting-state-with-a-key
  - Then you need to run the page with `npm run dev` otherwise it won't appear.
- update `newNote` so it reflects the current value of the input

```
const addNote = (event) => {
  event.preventDefault()
  const noteObject = {
    content: newNote,
    important: Math.random() < 0.5,
    id: String(notes.length + 1),
  }

  setNotes(notes.concat(noteObject))
  setNewNote('')
}
```
- we must never mutate state directly in React!

### Filtering Displayed Elements

- Only display the important notes

`  const [showAll, setShowAll] = useState(true) `

```
  const notesToShow = showAll
    ? notes
    : notes.filter(note.important === true)
```
### exercises
#### 2.6
- that took too long
#### 2.7
```
    if (persons.filter(p => p.name === newName).length !== 0) {
      alert(`${newName} is already in the phonebook`)
      return
    }
```
#### 2.8
- tick
#### 2.9

#### 2.10
- needed a little chatGPT help there, but I think I got it. Turns out you have to pass teh data and the handler to the component in its file. It should be dumb, and not do any data processing though.
## [c => Getting data from server](https://fullstackopen.com/en/part2/getting_data_from_server)
### The browser as a runtime environment
### npm
### Axios and promises
### Effect-hooks
### The development runtime environment
### Exercises
#### 2.11
## [d => Alternating data in server](https://fullstackopen.com/en/part2/altering_data_in_server)
### REST
### Sending Data to the Server
### Changing the Importance of Notes
### Extracting Communication with the Backend into a Separate Module
### Cleaner Syntax for Defining Object Literals
### Promises and Errors
### Full stack developer's oath
### Exercises
#### 2.12
#### 2.13
#### 2.14
#### 2.15
## [e => Adding styles to React app](https://fullstackopen.com/en/part2/adding_styles_to_react_app)
### Improved error message
### Inline styles
### Exercises
#### 2.16
#### 2.17
### Couple of important remarks
### Exercises
#### 2.18
#### 2.19
#### 2.20


