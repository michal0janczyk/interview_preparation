#pragma once

#include "Board.hpp"
#include "OutputHandler.hpp"

class OutputHandler
{
public:
	static const int height = 30, width = 30;

	void dump(const int * const *tab);

};

