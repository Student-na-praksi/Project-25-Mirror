"use client";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Switch } from "@/components/ui/switch";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import React from "react";

export type MyCard = {
  id: number;
  time: string;
  subject: string;
  day: string;
  lectureIndex: number;
  lectureTitle: string;
  originalFile: File | null;
  txtFile: File | null;
};

// Function to generate lectureTitle
const generateLectureTitle = (subject: string, lectureIndex: number) => {
  return `${subject} ${lectureIndex}`;
};

// Your original data
const data = [
  { id: 1, time: "10:00-12:00", subject: "Math", day: "Monday", lectureIndex: 1 },
  { id: 2, time: "11:00-14:00", subject: "English", day: "Tuesday", lectureIndex: 2 },
  {
    id: 3,
    time: "12:00",
    subject: "Science",
    day: "Wednesday",
    lectureIndex: 3,
  },
  // ... more items ...
];

// Map the data to Card array
const cards: MyCard[] = data.map((item) => ({
  ...item,
  lectureTitle: generateLectureTitle(item.subject, item.lectureIndex),
  originalFile: null,
  txtFile: null,
}));

const tedenskiUrnik = "TEDENSKI URNIK";
const pegledPredmeta = "PREGLED PREDMETA";

export default function TableDemo() {
  const [title, setTitle] = React.useState(tedenskiUrnik);

  const handleSwitchChange = (checked: boolean) => {
    if (checked) {
      setTitle(pegledPredmeta);
    } else {
      setTitle(tedenskiUrnik);
    }
  };

return (
    <div>
        <h1>{title}</h1>
        <Switch
            //checked=true //{switch.value}
            onCheckedChange={handleSwitchChange}
        />
        {title === tedenskiUrnik ? (
            <div style={{ display: "flex", justifyContent: "space-between" }}>
                {/* Render 5 tables side by side */}
                {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].map((day, index) => {
                    const filteredCards = cards.filter(card => card.day === day);
                    return (
                        <div key={index}>
                            <h2>{day}</h2>
                            <Table>
                                <TableCaption>A list of your recent lectures.</TableCaption>
                                <TableHeader>
                                    <TableRow>
                                        <TableHead>Time</TableHead>
                                        <TableHead>Subject</TableHead>
                                        <TableHead>Lecture Title</TableHead>
                                    </TableRow>
                                </TableHeader>
                                <TableBody>
                                    {filteredCards.map((card) => (
                                        <React.Fragment key={card.id}>
                                            <TableRow>
                                                <TableCell>{card.time}</TableCell>
                                                <TableCell>{card.subject}</TableCell>
                                                <TableCell>{card.lectureTitle}</TableCell>
                                            </TableRow>
                                            <TableRow>
                                                <TableCell colSpan={4}>
                                                    <Button onClick={() => console.log("Button clicked!")}>Naloži zapiske</Button>
                                                </TableCell>
                                            </TableRow>
                                        </React.Fragment>
                                    ))}
                                </TableBody>
                            </Table>
                        </div>
                    );
                })}
            </div>
        ) : (
            cards.map((card) => (
                <div key={card.id}>
                    <h2>{card.subject}</h2>
                    <Table>
                        <TableCaption>A list of your recent lectures.</TableCaption>
                        <TableHeader>
                            <TableRow>
                                <TableHead>Time</TableHead>
                                <TableHead>Subject</TableHead>
                                <TableHead>Day</TableHead>
                                <TableHead>Lecture Title</TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            <TableRow key={card.id}>
                                <TableCell>{card.time}</TableCell>
                                <TableCell>{card.subject}</TableCell>
                                <TableCell>{card.day}</TableCell>
                                <TableCell>{card.lectureTitle}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell colSpan={4}>
                                    <Button onClick={() => console.log("Button clicked!")}>Naloži zapiske</Button>
                                </TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </div>
            ))
        )}
    </div>
);}
