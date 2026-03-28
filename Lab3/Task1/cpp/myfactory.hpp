#pragma once

#include <string>
#include <map>
#include <vector>
#include <functional>
#include <memory>

/*
Template functions and classes aren't compiled until they are used with a specific type (template instantiation).
So the compiler must see the full definition of the template (not just the declaration) at the point of instantiation.
If the logic is in a .cpp file, the compiler won't see it at that point, but it can see what's in an included header file at any point.
(could also use a .tpp)
*/

class MyFactory {
    public:
        static MyFactory& instance();   // Singleton

        template<typename Base>
        // using instead of typedef because it allows templates
        using CreatorFunc = std::function<std::unique_ptr<Base>(const std::string&)>;   // A function that creates a unique_ptr to an object of type Base from a string identifier.

        // Register a creator function for a specific type Base with an identifier
        template<typename Base>
        int registerCreator(const std::string& id, CreatorFunc<Base> creator) { // Has to return an int for automatic registration to be possible
            auto& map = getMap<Base>();
            map[id] = creator;
            return 0;
        }

        // Create an object of type Base using the registered creator function and an identifier
        template<typename Base>
        std::unique_ptr<Base> create(const std::string& id, const std::string& arg) {
            auto& map = getMap<Base>();
            if (map.contains(id)) {
                return map[id](arg);
            } else {
                return nullptr;
            }
        }

        template<typename Base>
        std::vector<std::string> getIds() {
            std::vector<std::string> ids;
            for (const auto& pair : getMap<Base>()) {
                ids.push_back(pair.first);
            }
            return ids;
        }

    private:
        MyFactory() = default;
        ~MyFactory() = default;

        // Prevent copying and assignment (singleton pattern)
        MyFactory(const MyFactory&) = delete;   
        MyFactory& operator=(const MyFactory&) = delete;

        // The map that holds the creator functions for each type
        template<typename Base>
        std::map<std::string, CreatorFunc<Base>>& getMap() {
            static std::map<std::string, CreatorFunc<Base>> inst;   // Static map to hold creator functions for each type Base
            return inst;
        }
};