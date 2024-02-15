#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match('#', line)         #Checks for hashtag (#)
        if match:
            continue                        #skips lines with any # in them


       # match = re.match('%')               #checks for the percent sign (%)
        fields = line.strip().split(':')    #strip any whitespace and split into an array

        if match or len(fields) != 5:       #if match is true (there is a percent sign) OR the length of fields is NOT 5, we skip those lines
                                            #Those lines are skipped because they are not valid users to add since they are either missing info or have symbols that shouldn't be there
            continue

        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3], fields[2])

        groups = fields[4].split(",")        #Splits the last field into a list of groups

        print("==> Creating account for %s ..." % (username))

        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd
        
        os.system(cmd)                      #Executes the adduser command to create a new account
        
        print("==> Setting the password for %s ..." % (username))

        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd

        os.system(cmd)                  #Sets the password for the new account

        for group in groups:            # the for loop is looking at each 'item' in groups one at a time
                                        # if the group is not equal to "-" then the if statement is true so we enter the if statement
                                        # the if statement will print out that it's assigning the 'group' (aka the user) it is looking at to a group
            if group != "-":
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)          #adds user to the specified group

        
if __name__ == '__main__':
    main()
