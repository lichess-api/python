import json


class Decoder(json.JSONDecoder):
    def decode(self, s: str, *args, **kwargs):
        lines = ",".join(s.splitlines())
        text = "[{}]".format(lines)
        return super(Decoder, self).decode(text, *args, **kwargs)


class Encoder(json.JSONEncoder):
    def encode(self, obj, *args, **kwargs):
        lines: list[str] = []
        for each in obj:
            line = super(Encoder, self).encode(each, *args, **kwargs)
            lines.append(line)
        return "\n".join(lines)


def load(*args, **kwargs):
    kwargs.setdefault("cls", Decoder)
    return json.load(*args, **kwargs)


def loads(*args, **kwargs):
    kwargs.setdefault("cls", Decoder)
    return json.loads(*args, **kwargs)


def dump(obj, fp, cls=None, **kwargs):
    if cls is None:
        cls = Encoder
    text = cls(**kwargs).encode(obj)
    fp.write(text)


def dumps(*args, **kwargs):
    kwargs.setdefault("cls", Encoder)
    return json.dumps(*args, **kwargs)


class writer:
    def __init__(self, f, **kwargs):
        self.f = f
        self.kwargs = kwargs

    def writerow(self, row):
        stringified = json.dumps(row, **self.kwargs)
        self.f.write(stringified + "\n")


class reader:
    def __init__(self, f, **kwargs):
        self.f = f
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        line = ""

        while line == "":
            line = next(self.f).strip()

        return json.loads(line, **self.kwargs)
