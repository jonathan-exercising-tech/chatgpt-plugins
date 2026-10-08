# Optional signature

The public template defaults to no signature and contains no preset personal profiles.
To opt in, create `signature.local.tex` beside your working `.tex` document:

```tex
\SetHandoutSignature{Example Teacher}
```

Use only values explicitly supplied for that document. Escape TeX special characters, for example `\_`, `\&`, and `\%`. To disable a configured signature, use `\SetHandoutSignatureProfile{none}`. Only `custom` and `none` are supported; legacy profile names produce no output.

Keep the private configuration outside the plugin folder. The repository ignores `signature.local.tex`; do not include it in shared source archives. A compiled PDF with an enabled signature intentionally contains that signature: inspect the footer before sharing. Long or multi-line signatures require visual collision checks.
