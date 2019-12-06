/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */

function main(params) {
  if (!params.name || !params.slug || !params.recommendedVersion) {
    return Promise.reject({ error: 'no name, slug, or recommendedVersion'});
  }
  return {
    doc: {
      createdAt: new Date(),
       name: params.name,
       slug: params.slug,
       recommendedVersion: params.recommendedVersion
    }
  };
}
