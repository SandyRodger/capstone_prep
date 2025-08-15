# [Typescript Setup with Node & Express](https://www.youtube.com/watch?v=zRo2tvQpus8)
(this is a very straight-forward tutorial, I don't need to memorize the steps -> 13 minutes)
- [01:38] `sudo npm i -g typescript`
- `touch app.ts`
- [2:09] create a const and an array
- Compile with `tsc`
- creates 'js' file
- defaults to `var` -> we can change that in the config file
- [3:17] linter notes errors, but it will still create the js file.
  -  [4:30]change target to `ES6` in config file
  -  change output directory `"outDir"
  -  and rootDir
- create config file with `tsc --int``
- [5:20] -> tsc now automatically uses teh src folder
- [6:00] install
- `npm i -D typescript tr-node nodemon`
- `start: "node dist/app.js"
- [08:00] Use import syntax:
  - -`import express from 'express';`
- [12:00] `npm run build` when you're ready to build.

# [React with TypeScript Crash Course](https://www.youtube.com/watch?v=jrKcJxF0lAU)

- 1 hour 7 mins
- [00:00] what is Typescript
  - [03:00] benefits:
    - catch errors early in development
    - serves as documentation
  - [05:00] learn by building this simple 'people invited to my party' app.
- [07:10] create a Typescript React app
  - create a standard react app: `npx create-react-app name-of-app`
  - create a typescript react app: `npx create-react-app --template typescript typescript-react-tutorial`
  - ... takes 90 seconds
  - go into the app
  - `npm start` (runs on local host:3000)
  - [09:30] looks like a normal react app, except in the `src` folder where the files end with `.tsx`

```App.tsx
import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [number, setNumber] = useState(5);

  const changeNumber = () => {
    setNumber("10") // typescript doesn't like this
  }
```

- [10:55] Handling State
  - [14:00] what if you want it to be a number or a type?

`const [number, setNumber] = useState<number | string>(5);`
  - [17:00]
```
  const [people, setPeople] = useState([{
    name: "boom",
    age: 35,
    note: "yeh"
  }]);
```
  - [20:00] what if you want to start with an empty array, but still have the types set?  use an interface
```
  interface IState {
    people: {
      name: string
      age: number
      url: string
      note?: string
    }[]
  }
  const [people, setPeople] = useState<IState["people"]>([
    {
      name: "boom",
      url: "",
      age: 35,
      note: "yeh"
    },
    {
      name: "boom",
      url: "",
      age: 35,
    },
  ]);
```

- [24:15] Handling props
  - Use the state we have set to render the cards
  - `mkdir src/components`
  - `code src/components/List.tsx`
- final form:

```List.tsx
import React from "react";

  interface IProps {
    people: {
      name: string
      age: number
      url: string
      note?: string
    }[]
  }

const List: React.FC<IProps> = () => {
  return (
    <div>
      I am a list
    </div>
  )
}

export default List
```

```App.tsx
import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import List from "./components/List"

function App() {

  interface IState {
    people: {
      name: string
      age: number
      url: string
      note?: string
    }[]
  }


  const [people, setPeople] = useState<IState["people"]>([
    {
      name: "boom",
      url: "",
      age: 35,
      note: "yeh"
    },
    {
      name: "boom",
      url: "",
      age: 35,
    },
  ]);

  return (
    <div className="App">
      <h1>People invited</h1>
      <List people={people}></List>
    </div>
  );
}

export default App;
```
- [31:08] Handling functions

- iterate over the peoplea array and render the cards
- copy css styles from `https://github.com/harblaith7/React-With-TypeScript-Crash-Course/blob/main/src/App.css`
- 

- [40:36] Handling events
