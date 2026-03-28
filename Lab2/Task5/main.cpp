#include <iostream>
#include <thread>
#include <chrono>

#include "NumberSequence.hpp"

#include "KeyboardSource.hpp"
#include "FileSource.hpp"

#include "FileLogAction.hpp"
#include "SumAction.hpp"
#include "AverageAction.hpp"
#include "MedianAction.hpp"

int main() {
    KeyboardSource* keyboardSource = new KeyboardSource();
    FileSource* fileSource = new FileSource("numbers_source.txt");

    FileLogAction* fileLogAction = new FileLogAction("log.txt");
    SumAction* sumAction = new SumAction();
    AverageAction* averageAction = new AverageAction();
    MedianAction* medianAction = new MedianAction();

    NumberSequence numberSequence = NumberSequence(fileSource);

    numberSequence.attachAction(fileLogAction);
    numberSequence.attachAction(sumAction);
    numberSequence.start();

    numberSequence.changeSource(keyboardSource);
    numberSequence.detachAction(sumAction);
    numberSequence.attachAction(averageAction);
    numberSequence.attachAction(medianAction);
    numberSequence.start();
    
    return 0;
}