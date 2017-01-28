

#calss header
class _ACTIVE():
	def __init__(self,): 
		self.name = "ACTIVE"
		self.definitions = [u'busy with a particular activity: ', u'involved in a particular activity: ', u'An active volcano is one that might erupt (= throw out hot liquid rock or other matter) at any time.', u'An active verb or sentence is one in which the subject is the person or thing that performs the stated action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
