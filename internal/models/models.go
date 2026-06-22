package models

import time

type Student struct {
	ID       uint   `gorm:"primaryKey"`
	Name     string

	Score    int
	Energy   int
	PetFood  int

	Pets      []Pet
	Tasks     []StudentTask
	Exchanges []ExchangeRecord

	CreatedAt time.Time
	UpdatedAt time.Time
}


type Pet struct {
	ID uint `gorm:"primaryKey"`

	StudentID uint `gorm:"index"`

	Name string

	Level int
	Exp   int

	Hunger int
	Mood   int

	CreatedAt time.Time
	UpdatedAt time.Time
}


type Task struct {
    ID uint

    Name string

    Description string

    TaskType string

    RewardScore int
    RewardEnergy int
    RewardPetFood int

    RepeatType string

    StartTime *time.Time

    EndTime *time.Time

    Enable bool
}


type StudentTask struct {
	ID uint `gorm:"primaryKey"`

	StudentID uint
	TaskID    uint

	Status string

	Score   int
	Energy  int
	PetFood int

	FinishedAt *time.Time
}



type Rule struct {
	ID uint `gorm:"primaryKey"`

	Name string

	NeedScore int

	RewardEnergy int
	RewardPetFood int
}

type ExchangeRecord struct {
    ID uint `gorm:"primaryKey"`

    StudentID uint
    RuleID    uint

    CostScore int

    GainEnergy int
    GainPetFood int

    Student Student
    Rule    Rule
}