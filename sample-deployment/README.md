### GRNsight Sample Deployment
This sample deployment can be used to simulate how GRNsight is embedded into an iframe when deployed to production.

#### Running the Sample Deployment
- In the command line, enter the `sample-deployment/sample-deployment-web-app` folder, making sure that you are outside of the `/public/` folder.
- When running the app for the first time, run `npm install` in the command line.
- In the command line, run `npm run start-dev`.
- `superstatic` has been configured to host GRNsight at `http://localhost:8080`.

#### Temporary Changes to Make to Local Version of GRNsight
- The `config.js` and `iframe-coordination.js` files are included in the `sample-deployment/` folder for reference to what the files should look like in the user's local version of GRNsight, but they are not directly executed by the sample deployment.
- In the sample files, anywhere that states `http://localhost:8080` should be the site hosting the sample deployment.
- The development and production configurations in GRNsight's `web-client/config/config.js` should look like the sample file in `sample-deployment/config.js`.
- The `iframe-coordination` file can be entirely copy and pasted from `sample-deployment/iframe-coordination.js` into the user's local version of GRNsight.
- The first line of `web-client/public/js/constants.js` should be changed to this:
```
export const HOST_SITE = "http://localhost:8080"
```