

#calss header
class _STANDARD():
	def __init__(self,): 
		self.name = "STANDARD"
		self.definitions = [u'usual rather than special, especially when thought of as being correct or acceptable: ', u'Language described as standard is the form of that language that is considered acceptable and correct by most educated users of it: ', u'A standard book or writer is the one that is most commonly read for information on a particular subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
