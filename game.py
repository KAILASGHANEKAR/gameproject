{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e22ca69d-928e-4e7d-9522-8313c1526684",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "o\n"
     ]
    }
   ],
   "source": [
    "k=(\"kailas is software engineer\")\n",
    "print(k[11])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "d680a5db-2171-4c1b-be33-3587f9266aaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "whats your name? kailas\n",
      "and your name? swati\n",
      "kailas, do yo want to chose rock, paper or scissors? rock\n",
      "swati, do yo want to chose rock, paper or scissors? paper\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "paper wins!\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "user1 = input(\"whats your name?\")\n",
    "user2 = input(\"and your name?\")\n",
    "user1_answer = input(\"%s, do yo want to chose rock, paper or scissors?\" % user1)\n",
    "user2_answer = input(\"%s, do yo want to chose rock, paper or scissors?\" % user2)\n",
    "def compare (u1,u2):\n",
    "    if u1==u2:\n",
    "        return(\"its a tie!\")\n",
    "    elif u1=='rock':\n",
    "        if u2== 'scissors':\n",
    "            return (\"rock wins!\")\n",
    "        else:\n",
    "            return(\"paper wins!\")\n",
    "    elif u1 == (\"scissors win!\"):\n",
    "        if u2 == 'scissors':\n",
    "            return (\"scissors win!\")\n",
    "        else:\n",
    "            return(\"paper wins!\")\n",
    "    elif u1 == 'paper':\n",
    "        if u2 == 'rock':\n",
    "            return(\"paper wins!\")\n",
    "        else:\n",
    "            return(\"scissors win!\")\n",
    "    else:\n",
    "        return(\"invalid input! you have not enter rock, paper or scissors,try again.\")\n",
    "        sys.exit()    \n",
    "print(compare(user1_answer, user2_answer))\n",
    "                \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
