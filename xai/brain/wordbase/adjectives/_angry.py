

#calss header
class _ANGRY():
	def __init__(self,): 
		self.name = "ANGRY"
		self.definitions = [u'having a strong feeling against someone who has behaved badly, making you want to shout at them or hurt them: ', u'An angry sea or sky is one where there is a storm, or where it looks as if there will be a storm soon.', u'If an infected area of the body is angry, it is red and painful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
