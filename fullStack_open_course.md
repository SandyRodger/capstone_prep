# [Full stack open course](https://fullstackopen.com/en/)

## [part 1 - Introduction to React](https://fullstackopen.com/en/part1)

### a Introduction to React

-  React is a JavaScript library
-  get started with Vite
-  Created by Facebook (now Meta)
-  Used for building user interfaces, especially single-page applications (SPAs)

#### Vite

npm create vite@latest introdemo --template react
- chose React and Javascript
npm create vite@latest introdemo -- --template react
  - I won't run this one because it says it's already installed

cd introdemo
npm install
npm run dev # to start the application

change `main.jsx` to:

```
import ReactDOM from 'react-dom/client'

import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
```
#### JSX

- The compilation is handled by Babel.
- tags must be closed: `<br />`
- root component called App at the top of the component tree

##### props: passing data to components

```
const Hello = (props) => {
  return (
    <div>
      <p>Hello {props.name}</p>
    </div>
  )
}
```

```
const App = () => {
  return (
    <div>
      <h1>Greetings</h1>
      <Hello name='George' />
      <Hello name='Daisy' />
    </div>
  )
}
```

- sing fragments, i.e. by wrapping the elements to be returned by the component with 2 empty elements:

```javascript
const App = () => {
  const name = 'Peter'
  const age = 10

  return (
    <>
      <h1>Greetings</h1>
      <Hello name='Maya' age={26 + 10} />
      <Hello name={name} age={age} />
      <Footer />
    </>
  )
}
```

###### Do not render objects

-  Objects are not valid as a React child -> they just don't get rendered and throw an error in the console.

-  In React, the individual things rendered in braces must be primitive values, such as numbers or strings:
```
const App = () => {
  const friends = [
    { name: 'Peter', age: 4 },
    { name: 'Maya', age: 10 },
  ]

  return (
    <div>
      <p>{friends[0].name} {friends[0].age}</p>
      <p>{friends[1].name} {friends[1].age}</p>
    </div>
  )
}

export default App
```

#### Exercises:

1. 

npm create vite@latest courseInformation -- --template react
Package name: fso_pt1_exercises

- change `main.jsx` to:

```
import ReactDOM from 'react-dom/client'

import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
```

- change `App.jsx` to:

```
const App = () => {
  const course = 'Half Stack application development'
  const part1 = 'Fundamentals of React'
  const exercises1 = 10
  const part2 = 'Using props to pass data'
  const exercises2 = 7
  const part3 = 'State of a component'
  const exercises3 = 14

  return (
    <div>
      <h1>{course}</h1>
      <p>
        {part1} {exercises1}
      </p>
      <p>
        {part2} {exercises2}
      </p>
      <p>
        {part3} {exercises3}
      </p>
      <p>Number of exercises {exercises1 + exercises2 + exercises3}</p>
    </div>
  )
}

export default App
```

MY ANSWER:

```
const App = () => {
  const course = 'Half Stack application development'
  const parts = ['Fundamentals of React', 'Using props to pass data', 'State of a component']
  const exercises = [10, 7, 14]

  const Header = () => (
    <h1>{course}</h1>
  )

  const Content = () => (
    <>
      <p>
        {parts[0]} {exercises[0]}
      </p>
      <p>
        {parts[1]} {exercises[1]}
      </p>
      <p>
        {parts[2]} {exercises[2]}
      </p>
    </>
  )

  const Total = () => {
    <>
      <p>
        Number of exercises {exercises.reduce((a, v) => a + v)}
      </p>
    </>
  }

  return (
    <div>
      <Header course={course} />
      <Content parts={parts} exercises={exercises} />
      <Total exercises={exercises}/>
    </div>
  )
}
```

1 b)

- already done.

### [b JavaScript](https://fullstackopen.com/en/part1/java_script)

- We're talking about how different versions of javascript are transipled in the browser to newer versions and the most popular way to do this is with Babel.
- Now we're talking about `Node.js`:
  - Its a javascript runtime environment based on Google's CHrome 8 javascript engine. It works practically anywhere.
- Javascript is not Java
#### Variables:
- skim
#### Arrays
- skim
#### Objects
- skip
#### Functions
- skip
#### Exercises

```
const App = () => {
  const course = 'Half Stack application development'
  const parts = [
    {
      name: 'Fundamentals of React',
      exercises: 10
    },
    {
      name: 'Using props to pass data',
      exercises: 7
    },
    {
      name: 'State of a component',
      exercises: 14
    }
  ]

  const Header = () => (
    <h1>{course}</h1>
  )

  const Content = () => (
    <>
      <p>
        {parts[0].name} {parts[0].exercises}
      </p>
      <p>
        {parts[1].name} {parts[1].exercises}
      </p>
      <p>
        {parts[2].name} {parts[2].exercises}
      </p>
    </> 
  )

  const Total = () => (
    <p>
      Number of exercises {parts.map(p => p.exercises).reduce((a, v) => a + v)}
    </p>
  )

  return (
    <div>
      <Header course={course} />
      <Content parts={parts} />
      <Total parts={parts}/>
    </div>
  )
}

export default App
```

#### Object methods and "this"

- something about 'React Hooks'

assigning methods to objects:

```
const arto = {
  name: 'Arto Hellas',
  age: 35,
  education: 'PhD',

  greet: function() {
    console.log('hello, my name is ' + this.name)
  },
}

arto.greet()  // "hello, my name is Arto Hellas" gets printed
```
- skim
- bind()
###### Classes
```
class Person {
  constructor(name, age) {
    this.name = name
    this.age = age
  }
  greet() {
    console.log('hello, my name is ' + this.name)
  }
}

const adam = new Person('Adam Ondra', 29)
adam.greet()

const janja = new Person('Janja Garnbret', 23)
janja.greet()
```

-skim
###### JavaScript materials
- a list of resources on the internet for learing JS.

### [c Component state, event handlers](https://fullstackopen.com/en/part1/component_state_event_handlers)

- start with this:
```
const Hello = (props) => {
  return (
    <div>
      <p>
        Hello {props.name}, you are {props.age} years old
      </p>
    </div>
  )
}

const App = () => {
  const name = 'Peter'
  const age = 10

  return (
    <div>
      <h1>Greetings</h1>
      <Hello name="Maya" age={26 + 10} />
      <Hello name={name} age={age} />
    </div>
  )
}
```
###### Component helper functions

```
const Hello = (props) => {

  const bornYear = () => {
    const yearNow = new Date().getFullYear()
    return yearNow - props.age
  }

  return (
    <div>
      <p>
        Hello {props.name}, you are {props.age} years old
      </p>

      <p>So you were probably born in {bornYear()}</p>
    </div>
  )
}
```

###### Destructuring

```
const Hello = (props) => {
  const { name, age } = props
```

###### Page re-rendering

```
const App = (props) => {
  const {counter} = props
  return (
    <div>{counter}</div>
  )
}

export default App
```

###### Stateful component (+ State Hook)



### d A more complex state, debugging React apps



## [part 2 Communicating with server](https://fullstackopen.com/en/about)
## [part 3  - programming a server with NodeJS and Express](https://fullstackopen.com/en/part3)
## [part 5 - Testing React Apps](https://fullstackopen.com/en/part5)
## [Part 7: React Router, custom hooks, styling app with CSS and webpack](https://fullstackopen.com/en/part7)
## part 7a
## part 7b
## [Part 9 - Typescript](https://fullstackopen.com/en/part9)
## part 9c
## part 9d


The goal of going through the FullStack Open course is to be able to code a simple React app, and becoming comfortable with the useState and useEffect hooks.
Remember to take notes as you make progress. This will help you quickly review concepts during the frameworks and integration phase of Capstone.

Important articles to read after you finish the course:

- Context Api
- useReducer Hook
- useCallback Hook
- useEffect Hook
Added by
