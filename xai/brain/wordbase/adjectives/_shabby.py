

#calss header
class _SHABBY():
	def __init__(self,): 
		self.name = "SHABBY"
		self.definitions = [u'looking old and in bad condition because of being used for a long time or not being cared for: ', u'not honourable or fair; unacceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
