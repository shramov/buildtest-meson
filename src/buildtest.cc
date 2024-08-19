#include "buildtest.h"

#include <fmt/format.h>

int buildtest_call(int v)
{
	fmt::print(">>> buildtest function called: {}\n", v);
	return v;
}
