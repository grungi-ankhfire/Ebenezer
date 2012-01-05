# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu

class AccountListMenu(Menu):

    def __init__(self, app, accounts):
        Menu.__init__(self, app)
        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "---------[ Accounts list ]----------"]

        self.contents = []
        index = 0
        for a in accounts:
            index += 1
            string = ""
            if a.props["name"] == self.app.active_account.props["name"]:
                string += "* "
            else:
                string += "  "

            string += str(index) + " " + a.props["name"]
            self.contents.append(string)
            self.answers[str(index)] = [self.set_active, index]

            self.footer = ["[1] to [" + str(index) + "] to set active account",\
                           "[A]dd an account",\
                           "[G]o back"]

        self.prompt = "What do you want to do ?"


        self.answers['g'] = [self.change_menu, "mainmenu"]
        self.answers['a'] = [self.add_account, index+1]


    def update(self):
        index = 0
        for a in self.app.accounts:
            index += 1
            string = ""
            if a.props["name"] == self.app.active_account.props["name"]:
                string += "* "
            else:
                string += "  "

            string += str(index) + " " + a.props["name"]
            self.contents[index-1] = string
        self.answers['a'] = [self.add_account, index]

    def set_active(self, data):
        self.app.active_account = self.app.accounts[data-1]

    def add_account(self, index):
        pass
