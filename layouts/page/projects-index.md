{{.Content}}

---

{{ range .site.data.projects }}
<h4>
    [{{.name}}:]({{.link}})&nbsp;
    {{ $len := (len $.languages) }}
    {{ range $index, $lang = .languages }}
    <small>{{ . }}</small>
    {{ if ne (add $index 1) $len }}, {{ end }}
    {{ end }}
</h4>
{{.description}}
{{ end }}

