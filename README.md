How to get data:


Yahoo
-----
Register for Yahoo Developer Network and get your credentials:
3.1) Register for a Yahoo account at https://yahoo.com/
3.2) Go to https://developer.yahoo.com/ --> 'My Apps' --> 'YDN Apps'
3.3) On the lefthand panel, click 'Create an App'
3.4) Name your app whatever you please ("Fantasy Football Stats") in the 'Application Name' block.
3.5) Select the 'Installed Application' option since we're only going to be accessing the data from our local machines.
3.6) Under the 'API Permissions' sections select 'Fantasy Sports' and then make sure that 'Read' is selected. 'Read/Write' would only be used if you wanted to be able to control your league via Python scripting vice just reading the data from your league. You can come back and change these options in the future.
3.7) The redirect uri can be https://oob for out of band meaning no uri
3.7) You have now successfully created a Yahoo Developer App and you will see App ID, Client ID(Consumer Key), and Client Secret(Consumer Secret) with a long string of random letters and numbers. Yahoo will use these keys to allow you to access it's API via OAuth 2.0.

