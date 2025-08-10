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

###### Stateful component

- state hook

```
import ReactDOM from 'react-dom/client'

import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
```

```
import { useState } from 'react'

const App = () => {

  const [ counter, setCounter ] = useState(0)


  setTimeout(
    () => setCounter(counter + 1),
    1000
  )

  return (
    <div>{counter}</div>
  )
}

export default App
```

###### Event handling

```
import { useState } from 'react'

const App = () => {

  const [ counter, setCounter ] = useState(0)

  const handleClick = () => {
    console.log('clicked')
  }

  return (
    <div>
      <div>{counter}</div>
      <button onClick={() => setCounter(counter + 1)}>
        plus
      </button>
      <button onClick={() => setCounter(0)}>
        zero
      </button>
    </div>
  )
}

export default App
```

### d A more complex state, debugging React apps

```
import { useState } from 'react'

const App = () => {

  const [ counter, setCounter ] = useState(0)

  const increaseByOne = () => setCounter(counter + 1)
  const setToZero = () => setCounter(0)

  return (
    <div>
      <div>{counter}</div>
      <button onClick={increaseByOne}>
        plus
      </button>
      <button onClick={setToZero}>
        zero
      </button>
    </div>
  )
}

export default App
```

###### Passing state - to child components

- "list the state up" in the component hierarchy (best practice) to their closest common ancestor.

```
import { useState } from 'react'

const Display = (props) => {
  return (
    <div>{props.counter}</div>
  )
}

const App = () => {

  const [ counter, setCounter ] = useState(0)

  const increaseByOne = () => setCounter(counter + 1)
  const decreaseByOne = () => setCounter(counter - 1)
  const setToZero = () => setCounter(0)

  const Button = (props) => {
    return (
      <button onClick={props.onClick}>
        {props.text}
      </button>
    )
  }

  return (
    <div>
      <Display counter={counter}/>
      <Button 
        onClick={increaseByOne}
        text='plus'
      />
      <Button 
        onClick={setToZero}
        text='zero'
      />
      <Button
        onClick={decreaseByOne}
        text='minus'
      />
    </div>
  )
}

export default App
```

###### Changes in state cause re-rendering
###### Refactoring the components

```
import { useState } from 'react'

const Display = ({counter}) => <div>{counter}</div>
const App = () => {

  const [ counter, setCounter ] = useState(0)

  const increaseByOne = () => setCounter(counter + 1)
  const decreaseByOne = () => setCounter(counter - 1)
  const setToZero = () => setCounter(0)

  const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>

  return (
    <div>
      <Display counter={counter}/>
      <Button 
        onClick={increaseByOne}
        text='plus'
      />
      <Button 
        onClick={setToZero}
        text='zero'
      />
      <Button
        onClick={decreaseByOne}
        text='minus'
      />
    </div>
  )
}

export default App
```

## [part 2 Communicating with server](https://fullstackopen.com/en/about)

##### Complex State

- "pieces of state"

```
const App = () => {
  const [left, setLeft] = useState(0)
  const [right, setRight] = useState(0)

  return (
    <div>
      {left}
      <button onClick={() => setLeft(left + 1)}>
        left
      </button>
      <button onClick={() => setRight(right + 1)}>
        right
      </button>
      {right}
    </div>
  )
}
```

- It is forbidden in React to mutate state directly.
##### Handling arrays

```
const App = () => {
  const [left, setLeft] = useState(0)
  const [right, setRight] = useState(0)

  const [allClicks, setAll] = useState([])


  const handleLeftClick = () => {
    setAll(allClicks.concat('L'))
    setLeft(left + 1)
  }


  const handleRightClick = () => {
    setAll(allClicks.concat('R'))
    setRight(right + 1)
  }

  return (
    <div>
      {left}
      <button onClick={handleLeftClick}>left</button>
      <button onClick={handleRightClick}>right</button>
      {right}

      <p>{allClicks.join(' ')}</p>
    </div>
  )
}
```
###### Update of the state is asynchronous

```
const App = () => {
  const [left, setLeft] = useState(0)
  const [right, setRight] = useState(0)
  const [allClicks, setAll] = useState([])

  const [total, setTotal] = useState(0)

  const handleLeftClick = () => {
    setAll(allClicks.concat('L'))
    setLeft(left + 1)

    setTotal(left + right)
  }

  const handleRightClick = () => {
    setAll(allClicks.concat('R'))
    setRight(right + 1)

    setTotal(left + right)
  }

  return (
    <div>
      {left}
      <button onClick={handleLeftClick}>left</button>
      <button onClick={handleRightClick}>right</button>
      {right}
      <p>{allClicks.join(' ')}</p>

      <p>total {total}</p>
    </div>
  )
}
```

- a state update in React happens asynchronously, i.e. not immediately but "at some point" before the component is rendered again.

###### Conditional rendering

```
import { useState } from 'react'

const History = (props) => {
  if (props.allClicks.length === 0) {
    return (
      <div>
        the app is used by pressing the buttons
      </div>
    )
  }
  return (
    <div>
      button press history: {props.allClicks.join(' ')}
    </div>
  )
}
const App = () => {
  const [left, setLeft] = useState(0)
  const [right, setRight] = useState(0)
  const [allClicks, setAll] = useState([])
  const [total, setTotal] = useState(0)

  const handleLeftClick = () => {
    setAll(allClicks.concat('L'))
    const updatedLeft = left + 1
    setLeft(updatedLeft)
    setTotal(updatedLeft + right)
  }

  const handleRightClick = () => {
    setAll(allClicks.concat('R'));
    const updatedRight = right + 1;
    setRight(updatedRight);
    setTotal(left + updatedRight);
  }

  return (
    <div>
      {left}
      <button onClick={handleLeftClick}>left</button>
      <button onClick={handleRightClick}>right</button>
      {right}
      <History allClicks={allClicks}/>
    </div>
  )
}

export default App
```

###### Old React

- state hook. Unavailable in older versions. Previous to that components that required state had to use class syntax.

###### Debugging React applications

- react developer tools extension for Chrome

###### Rules of Hooks

- hooks-based state functions
- `useState` must not be called from within:
  -  a loop
  -  a conditional expression
  -  anywhere not a function defining a component.
-  This is because we have to have the hooks called in the same order.

```
const App = () => {
  // these are ok
  const [age, setAge] = useState(0)
  const [name, setName] = useState('Juha Tauriainen')

  if ( age > 10 ) {
    // this does not work!
    const [foobar, setFoobar] = useState(null)
  }

  for ( let i = 0; i < age; i++ ) {
    // also this is not good
    const [rightWay, setRightWay] = useState(false)
  }

  const notGood = () => {
    // and this is also illegal
    const [x, setX] = useState(-1000)
  }

  return (
    //...
  )
}
```

#### What is useState? -> lsbot

- useState is a ​Hook​ in React that allows you to add state to functional components. In Object-Oriented Programming, you're used to managing state with instance properties (e.g., this.name). In React's functional components, useState provides a similar capability.
- When you call useState, it does two things:
  1.  It creates a "state variable" to hold a value between function calls (renders).
  2.  It gives you a function to update this value and trigger a re-render of your component.

- How does it work?
  - useState returns an array with exactly two elements, which you typically destructure:

```
import React, { useState } from 'react';

function Counter() {
  // 1. Call useState with the initial state value (e.g., 0).
  // 2. Destructure the returned array into a state variable and a setter function.
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      {/* When the button is clicked, call the setter function to update state */}
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

In this example:
•   useState(0) initializes the state with 0.
•   count is the state variable. Its initial value is 0.
•   setCount is the function you use to update the count state.
•   When setCount is called, React re-renders the Counter component, and the p tag will display the new count value.
It's important to remember that you should never modify the state variable directly (e.g., count = count + 1). Always use the setter function provided by useState to ensure React knows to update the UI.

************3:18 pm************************************************************

###### Event Handling Revisited

```
const App = () => {
  const [value, setValue] = useState(10)

  const handleClick = () =>
    console.log('clicked the button')

  return (
    <div>
      {value}
      <button onClick={handleClick}>button</button>
    </div>
  )
}
```
###### A function that returns a function

```
const hello = (who) => () => {
  console.log('hello', who)
}
```

```
const App = () => {
  const [value, setValue] = useState(10)
  

  const setToValue = (newValue) => () => {
    console.log('value now', newValue)  // print the new value to console
    setValue(newValue)
  }
  
  return (
    <div>
      {value}

      <button onClick={setToValue(1000)}>thousand</button>
      <button onClick={setToValue(0)}>reset</button>
      <button onClick={setToValue(value + 1)}>increment</button>
    </div>
  )
}
```
###### Passing Event Handlers to Child Components
```
const App = (props) => {
  // ...
  return (
    <div>
      {value}

      <Button onClick={() => setToValue(1000)} text="thousand" />
      <Button onClick={() => setToValue(0)} text="reset" />
      <Button onClick={() => setToValue(value + 1)} text="increment" />
    </div>
  )
}
```
###### Do Not Define Components Within Components

- Never define components inside of other components (even thouhg they appear to work).

```
const Display = props => <div>{props.value}</div>

const Button = (props) => (
  <button onClick={props.onClick}>
    {props.text}
  </button>
)

const App = () => {
  const [value, setValue] = useState(10)

  const setToValue = newValue => {
    console.log('value now', newValue)
    setValue(newValue)
  }

  return (
    <div>
      <Display value={value} />
      <Button onClick={() => setToValue(1000)} text="thousand" />
      <Button onClick={() => setToValue(0)} text="reset" />
      <Button onClick={() => setToValue(value + 1)} text="increment" />
    </div>
  )
}
```
###### Utilization of Large language models

- "Everyone knows that debugging is twice as hard as writing a program in the first place. SO if you're as clever as you can be when you write it, how will you ever debug it?" - Brian Kernighan.

### exercises:
1. 
```
import { useState } from 'react'

const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>
const App = () => {

  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)


  return (
    <div>
      <h1>give feedback</h1>
      <Button 
        onClick={() => setGood(good + 1)}
        text='good'
      />
      <Button 
        onClick={() => setNeutral(neutral + 1)}
        text='neutral'
      />
      <Button 
        onClick={() => setBad(bad + 1)}
        text='bad'
      />
      <h1>statistics</h1>
      <div>Goods: {good}</div>
      <div>Neutral: {neutral}</div>
      <div>Bad: {bad}</div>
    </div>
  )
}

export default App
```
2.
```
import { useState } from 'react'

const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>
const Display = ({counter, text}) => <div>{text} : {counter}</div>
const total = (...nums) => nums.reduce((v, a) => v + a)
const average = (good, neutral, bad) => (good - bad) / total(good, neutral, bad)
const positive = (good, neutral, bad) => (good/total(good, neutral, bad)) * 100

const App = () => {

  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  return (
    <div>
      <h1>give feedback</h1>
      <Button 
        onClick={() => setGood(good + 1)}
        text='good'
      />
      <Button 
        onClick={() => setNeutral(neutral + 1)}
        text='neutral'
      />
      <Button 
        onClick={() => setBad(bad + 1)}
        text='bad'
      />
      <h1>statistics</h1>
      <Display counter={good} text='good'/>
      <Display counter={neutral} text='neutral'/>
      <Display counter={bad} text='bad'/>
      <Display counter={total(good, bad, neutral)} text='all'/>
      <Display counter={average(good, neutral, bad)} text='average'/>
      <Display counter={positive(good, neutral, bad)} text='positive'/>
    </div>
  )
}

export default App
```

3. 
```
import { useState } from 'react'

const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>
const Display = ({counter, text}) => <div>{text} : {counter}</div>
const total = (...nums) => nums.reduce((v, a) => v + a)
const average = (good, neutral, bad) => (good - bad) / total(good, neutral, bad)
const positive = (good, neutral, bad) => (good/total(good, neutral, bad)) * 100
const Statistics = ({good, bad, neutral}) => {
  return (
    <div>
      <h1>statistics</h1>
      <Display counter={good} text='good'/>
      <Display counter={neutral} text='neutral'/>
      <Display counter={bad} text='bad'/>
      <Display counter={total(good, bad, neutral)} text='all'/>
      <Display counter={average(good, neutral, bad)} text='average'/>
      <Display counter={positive(good, neutral, bad)} text='positive'/>
    </div>
)}

const App = () => {

  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  return (
    <div>
      <h1>give feedback</h1>
      <Button 
        onClick={() => setGood(good + 1)}
        text='good'
      />
      <Button 
        onClick={() => setNeutral(neutral + 1)}
        text='neutral'
      />
      <Button 
        onClick={() => setBad(bad + 1)}
        text='bad'
      />
      <Statistics good={good} neutral={neutral} bad={bad}/>
    </div>
  )
}

export default App
```

4.
```
import { useState } from 'react'

const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>
const Display = ({counter, text}) => <div>{text} : {counter}</div>
const total = (...nums) => nums.reduce((v, a) => v + a)
const average = (good, neutral, bad) => (good - bad) / total(good, neutral, bad)
const positive = (good, neutral, bad) => (good/total(good, neutral, bad)) * 100
const Statistics = ({good, bad, neutral}) => {
  if (good || neutral || bad) {
  return (
    <div>
      <h1>statistics</h1>
      <Display counter={good} text='good'/>
      <Display counter={neutral} text='neutral'/>
      <Display counter={bad} text='bad'/>
      <Display counter={total(good, bad, neutral)} text='all'/>
      <Display counter={average(good, neutral, bad)} text='average'/>
      <Display counter={positive(good, neutral, bad)} text='positive'/>
    </div>
)} else {
  return (
    <div>
      <h1>statistics</h1>
      <div>No feedback given</div>
    </div>
  )
}}

const App = () => {

  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  return (
    <div>
      <h1>give feedback</h1>
      <Button 
        onClick={() => setGood(good + 1)}
        text='good'
      />
      <Button 
        onClick={() => setNeutral(neutral + 1)}
        text='neutral'
      />
      <Button 
        onClick={() => setBad(bad + 1)}
        text='bad'
      />
      <Statistics good={good} neutral={neutral} bad={bad}/>
    </div>
  )
}

export default App
```

5.
```
import { useState } from 'react'

const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>
const StatisticLine = ({counter, text}) => <div>{text} : {counter} {text === 'positive' ? '%' : ''}</div>
const total = (...nums) => nums.reduce((v, a) => v + a)
const average = (good, neutral, bad) => (good - bad) / total(good, neutral, bad)
const positive = (good, neutral, bad) => (good/total(good, neutral, bad)) * 100
const Statistics = ({good, bad, neutral}) => {
  if (good || neutral || bad) {
  return (
    <div>
      <h1>statistics</h1>
      <StatisticLine counter={good} text='good'/>
      <StatisticLine counter={neutral} text='neutral'/>
      <StatisticLine counter={bad} text='bad'/>
      <StatisticLine counter={total(good, bad, neutral)} text='all'/>
      <StatisticLine counter={average(good, neutral, bad)} text='average'/>
      <StatisticLine counter={positive(good, neutral, bad)} text='positive'/>
    </div>
)} else {
  return (
    <div>
      <h1>statistics</h1>
      <div>No feedback given</div>
    </div>
  )
}}

const App = () => {

  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  return (
    <div>
      <h1>give feedback</h1>
      <Button 
        onClick={() => setGood(good + 1)}
        text='good'
      />
      <Button 
        onClick={() => setNeutral(neutral + 1)}
        text='neutral'
      />
      <Button 
        onClick={() => setBad(bad + 1)}
        text='bad'
      />
      <Statistics good={good} neutral={neutral} bad={bad}/>
    </div>
  )
}

export default App
```

6.
```
import { useState } from 'react'

const Button = ({onClick, text}) => <button onClick={onClick}>{text}</button>
const StatisticLine = ({counter, text}) => <tr><td>{text}</td><td>{counter}{text === 'positive' ? '%' : ''}</td></tr>
const total = (...nums) => nums.reduce((v, a) => v + a)
const average = (good, neutral, bad) => (good - bad) / total(good, neutral, bad)
const positive = (good, neutral, bad) => (good/total(good, neutral, bad)) * 100
const Statistics = ({good, bad, neutral}) => {
  if (good || neutral || bad) {
  return (
    <>
      <h1>statistics</h1>
      <StatisticLine counter={good} text='good'/>
      <StatisticLine counter={neutral} text='neutral'/>
      <StatisticLine counter={bad} text='bad'/>
      <StatisticLine counter={total(good, bad, neutral)} text='all'/>
      <StatisticLine counter={average(good, neutral, bad)} text='average'/>
      <StatisticLine counter={positive(good, neutral, bad)} text='positive'/>
    </>
)} else {
  return (
    <div>
      <h1>statistics</h1>
      <div>No feedback given</div>
    </div>
  )
}}

const App = () => {

  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  return (
    <div>
      <h1>give feedback</h1>
      <Button 
        onClick={() => setGood(good + 1)}
        text='good'
      />
      <Button 
        onClick={() => setNeutral(neutral + 1)}
        text='neutral'
      />
      <Button 
        onClick={() => setBad(bad + 1)}
        text='bad'
      />
      <Statistics good={good} neutral={neutral} bad={bad}/>
    </div>
  )
}

export default App
```
7.
```
import { useState } from 'react'

const App = () => {
  const anecdotes = [
    'If it hurts, do it more often.',
    'Adding manpower to a late software project makes it later!',
    'The first 90 percent of the code accounts for the first 90 percent of the development time...The remaining 10 percent of the code accounts for the other 90 percent of the development time.',
    'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.',
    'Premature optimization is the root of all evil.',
    'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.',
    'Programming without an extremely heavy use of console.log is same as if a doctor would refuse to use x-rays or blood tests when diagnosing patients.',
    'The only way to go fast, is to go well.'
  ]
   
  const [selected, setSelected] = useState(0)
  const handleClick = () => {
    const index = Math.round(Math.random() * (anecdotes.length - 1))
    setSelected(index)
  }

  return (
    <>
      <button onClick={handleClick}>Click for another</button>
      <br></br>
      {anecdotes[selected]}
    </>
  )
}

export default App
```

1.13 : step 2:

```import { useState } from 'react'

const App = () => {
  const anecdotes = [
    'If it hurts, do it more often.',
    'Adding manpower to a late software project makes it later!',
    'The first 90 percent of the code accounts for the first 90 percent of the development time...The remaining 10 percent of the code accounts for the other 90 percent of the development time.',
    'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.',
    'Premature optimization is the root of all evil.',
    'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.',
    'Programming without an extremely heavy use of console.log is same as if a doctor would refuse to use x-rays or blood tests when diagnosing patients.',
    'The only way to go fast, is to go well.'
  ]

  const votes = Array.from({length: anectodes.length}, 0) 
  const [selected, setSelected] = useState(0)
  const newIndex = () => setSelected(Math.round(Math.random() * (anecdotes.length - 1)))
  const upvote = () => {console.log(votes)}

  return (
    <>
      {anecdotes[selected]}
      <div>has {votes}votes</div>
      <br></br>
      <button onClick={upvote}>vote</button>
      <button onClick={newIndex}>next anecdote</button>
    </>
  )
}

export default App
```

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
  
