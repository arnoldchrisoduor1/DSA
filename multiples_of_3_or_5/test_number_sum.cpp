#include "number_sum.h"
#include <gtest/gtest.h>

TEST(SolutionTest, NegativeInput) {
    EXPECT_EQ(Solution(-1), 0);
}

TEST(SolutionTest, ZeroInput) {
    EXPECT_EQ(Solution(0), 0);
}

TEST(SolutionTest, PositiveInput) {
    EXPECT_EQ(Solution(10), 23);
    EXPECT_EQ(Solution(20), 78);
}