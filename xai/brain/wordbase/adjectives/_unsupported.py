

#calss header
class _UNSUPPORTED():
	def __init__(self,): 
		self.name = "UNSUPPORTED"
		self.definitions = [u"If someone's opinions or statements are unsupported, they do not have any proof or evidence to show that they are true: ", u'not receiving any help or encouragement from other people: ', u'An unsupported structure or object does not use any other object or person to support its weight, especially from below to stop it from falling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
