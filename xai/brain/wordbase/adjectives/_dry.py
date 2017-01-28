

#calss header
class _DRY():
	def __init__(self,): 
		self.name = "DRY"
		self.definitions = [u'used to describe something that has no water or other liquid in, on, or around it: ', u'If a river or other area of water runs dry, the water gradually disappears from it: ', u'Dry hair or skin does not have enough of the natural oils that make it soft and smooth: ', u'Dry bread is plain, without butter, jam, etc.: ', u'If a book, talk, subject, etc. is dry, it is not interesting.', u'without alcoholic drinks: ', u'If wine or other alcoholic drinks are dry, they do not taste sweet: ', u'Dry humour is very funny in a way that is clever and not obvious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
