

#calss header
class _UNACCOMPANIED():
	def __init__(self,): 
		self.name = "UNACCOMPANIED"
		self.definitions = [u'not having anyone with you when you go somewhere: ', u'Unaccompanied music is produced by a singer or by someone playing a musical instrument without anyone else singing or playing at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
