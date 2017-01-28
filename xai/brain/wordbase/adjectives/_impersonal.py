

#calss header
class _IMPERSONAL():
	def __init__(self,): 
		self.name = "IMPERSONAL"
		self.definitions = [u'without human warmth; not friendly and without features that make people feel interested or involved: ', u'not referring to people or a particular person by name: ', u'An impersonal verb or sentence has the subject "it" and does not refer to a particular person or thing, as in the sentence It\'s cold outside.', u'not existing as a person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
