

#calss header
class _RELATIVE():
	def __init__(self,): 
		self.name = "RELATIVE"
		self.definitions = [u'being judged or measured in comparison with something else: ', u'true to a particular degree when compared with other things: ', u'If something is relative to something else, it changes according to the speed or level of the other thing: ', u'If something is relative to a particular subject, it is connected with it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
