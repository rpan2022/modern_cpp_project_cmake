#include <gtest/gtest.h>

#include <nlohmann/json.hpp>

using json = nlohmann::json;

TEST(JsonTest, BasicTest) {
  json j;
  j["key"] = "value";
  EXPECT_EQ(j["key"], "value");
}

TEST(MathTest, AddTest) { EXPECT_EQ(1 + 1, 2); }
